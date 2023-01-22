import time
import asyncio
from abc import ABC, abstractmethod # HELL

from asyncio.windows_events import ProactorEventLoop
from asyncio.events import AbstractEventLoop

class SelfPurgingObject(ABC): # You make this the parent, you like extend from it maybe??
    """
    The object will be auto purged from memory after a set amount of time, make sure the object has a __del__ function that handles saving if that is needed
    Requires the main function to use async
    """
    def __init__(self,event_loop: ProactorEventLoop | AbstractEventLoop, time_till_purge_in_seconds: int, reset_timer_if_accessed: bool = True):
        self.event_loop = None
        self.purge_time_delay = time_till_purge_in_seconds
        self.reset_time_if_accessed = reset_timer_if_accessed
        self.time_to_be_deleted = None
        self.current_event_loop_call = None
        if event_loop is not None:
            self.setup_part_2(event_loop)


    def setup_part_2(self, event_loop: ProactorEventLoop | AbstractEventLoop):
        self.event_loop = event_loop
        self.time_to_be_deleted = self.event_loop.time() + self.purge_time_delay
        self.schedule_deletion_for_purge_time()

    def reset_timer(self):
        if self.reset_time_if_accessed:
            self.time_to_be_deleted = self.event_loop.time() + self.purge_time_delay
            self.schedule_deletion_for_purge_time()
        else:
            pass # Don't reset timer duh

    def __delete_object(self):
        self._save(True) # SAVE
        del self # Make sure we are deleted

    def delete_if_time_finished_passing(self):
        if self.event_loop.time() >= self.time_to_be_deleted - 5: # 5 seconds just in case it calls it like a millisecond beforehand
            self.__delete_object()
        else:
            print("Not ready to be deleted")

    def schedule_deletion_for_purge_time(self):
        if self.current_event_loop_call is not None:
            try:
                self.current_event_loop_call.cancel()
            except():
                pass
        if self.time_to_be_deleted is not None:
            self.current_event_loop_call = self.event_loop.call_at(self.time_to_be_deleted, self.delete_if_time_finished_passing)
        else:
            pass

    @abstractmethod
    def _save(self, auto = False):
        """Called by the on del function, must be overriden, if you wish not use it just have pass in the function"""
        pass

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['event_loop']
        del state['current_event_loop_call']
        del state['time_to_be_deleted']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)