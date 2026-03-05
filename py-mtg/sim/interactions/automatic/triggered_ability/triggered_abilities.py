from ability_triggers import AbilityTriggerEnum
from typing import ByteString, Callable

class TriggeredAbility(Interaction):
    """
    Any type of trigger, EtB, Coin Flip, etc.
    E.g.:
        - Whenever you cast a spell.
        - Landfall.
        - Whenever a creature enters.
    """
    def __init__(self, source: gen_type, speed: Speed, effect: Effect, trigger_type: AbilityTriggerEnum, *args, **kwargs):
        super(self, source, speed, effect)
        self._trigger_type = trigger_type

    @property
    def trigger_type(self)->AbilityTriggerEnum:
        return self._trigger_type.copy()

class ConditionalTriggeredAbility(Trigger):
    """
    Any trigger which has to have conditions met.
    E.g.:
        - EtB for a card type
        - Effects that trigger on/after Nth effect.
    """

    @abstractmethod
    def _check_condition(self, cause: , *arg, **kwargs) -> bool:

    @abstractmethod
    def _effect(self, cause_uuid: bytes, *args, **kwargs):

    @abstractmethod
    def resolve(self, cause_uuid, *args, **kwargs):

