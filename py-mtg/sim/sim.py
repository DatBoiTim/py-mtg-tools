from interactions.automatic.ability_triggers import AbilityTriggerEnum
from interactions.automatic.triggered_ability.triggered_abilities import triggered_abilities
from interactions.interaction import Interaction
from uuid import UUID

class ActionStack:
    """
        The stack, where every action goes. 
        Operations against the stack must be idempotent.
        Shallow Copies only.
    """
    def __init__(self):
        self._stack: list[Interaction] = []

    @property
    def stack(self)->list[interaction]:
        return self._stack.copy()

    @stack.setter
    def stack(self, new: Self)->None:
        self._stack = new.copy()

class TriggerDictionary:

    def __init__(self, trigger: AbilityTriggerEnum):
        self._trigger = trigger
        self._trigger_list: dict[UUID, TriggeredAbility] = []

    @property
    def trigger(self)->AbilityTriggerEnum:
        return self._trigger

    @property
    def trigger_list(self)->list[TriggeredAbility]:
        return self._trigger_list

    @trigger_list.setter
    def trigger_list(self, new: dict[UUID, TriggeredAbility])->None:
        self._trigger_list = new.copy()

class TriggerRegistryByTrigger:
    def __init__(self):
        self._triggers_by_type: dict[AbilityTriggerEnum, TriggerDictionary] = {}

    def get_triggers_by_type(self, trigger: AbilityTriggerEnum)->TriggerDictionary|None:
        if trigger in self._triggers_by_type.keys():
            return self._triggers_by_type[trigger].copy()
        return None

    def set_triggers_by_type(self, trigger: AbilityTriggerEnum, triggers: TriggerDictionary)->None:
        if trigger in self._triggers_by_type.keys():
            self._triggers_by_type[trigger] = triggers

