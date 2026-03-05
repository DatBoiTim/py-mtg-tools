# TODO: Game Object with Triggers
from abc import ABC
from enum import Enum
from uuid import uuid4, UUID
from typing import Callable, Self

class Speed(Enum):
    AUTO = 1 # Basically Triggers
    PRTY = 2 # Instant Speed
    SORC = 3 # Sorcery Speed

gen_type = TypeVar('T')

class Effect(ABC)
    def __init__(self, source: Interaction, func: Callable[[list, dict], bool]):
        self._source = source
        self._func = func

    @classmethod
    def copy(origin: Self)->Self:
        self._source = origin.source
        self._func  = origin.func.copy()

    @property
    def source(self)->Interaction:
        return self._source

    @property
    def func(self)->Callable[[list,dict],bool]:
        return self._func.copy()

    @func.setter
    def func(self, new: Callable[[list,dict],bool])->None:
        self._func = new.copy()

    @abstractmethod
    def _resolve_triggers(self)->bool:

    @abstractmethod
    def resolve(self)->bool:

class Interaction(ABC):
    source: gen_type # Can be another ability of a permanent, a permanent, a spell, etc.
    uuid: UUID
    speed: Speed

    def __init__(self, source: gen_type, speed: Speed, effect: Effect, *args, **kwargs):
        self._uuid = uuid4() # Truly random to prevent collisions.
        self._source = source
        self._speed = Speed
        self._effect = effect

    @property
    def effect(self)->Effect:
        return self._effect.copy()

