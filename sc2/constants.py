from .data import Alliance, Attribute, CloakState, DisplayType, TargetType, Race
from .ids.ability_id import AbilityId
from .ids.ability_id import *
from .ids.buff_id import *
from .ids.effect_id import *
from .ids.unit_typeid import UnitTypeId
from .ids.unit_typeid import *
from .ids.upgrade_id import *
from collections import defaultdict
from typing import Dict, Set

mineral_ids: Set[int] = {
    146,  # RICHMINERALFIELD.value,
    147,  # RICHMINERALFIELD750.value,
    341,  # MINERALFIELD.value,
    1982,  # MINERALFIELD450.value,
    483,  # MINERALFIELD750.value,
    665,  # LABMINERALFIELD.value,
    666,  # LABMINERALFIELD750.value,
    796,  # PURIFIERRICHMINERALFIELD.value,
    797,  # PURIFIERRICHMINERALFIELD750.value,
    884,  # PURIFIERMINERALFIELD.value,
    885,  # PURIFIERMINERALFIELD750.value,
    886,  # BATTLESTATIONMINERALFIELD.value,
    887,  # BATTLESTATIONMINERALFIELD750.value,
    1983,  # MINERALFIELDOPAQUE.value,
    1984,  # MINERALFIELDOPAQUE900.value,
}

geyser_ids: Set[int] = {
    342,  # VESPENEGEYSER.value,
    343,  # SPACEPLATFORMGEYSER.value,
    344,  # RICHVESPENEGEYSER.value,
    608,  # PROTOSSVESPENEGEYSER.value,
    880,  # PURIFIERVESPENEGEYSER.value,
    881,  # SHAKURASVESPENEGEYSER.value,
}

race_worker: Dict[Race, UnitTypeId] = {
    Race.Protoss: UnitTypeId(84),  # UnitTypeId.PROBE,
    Race.Terran: UnitTypeId(45),  # UnitTypeId.SCV,
    Race.Zerg: UnitTypeId(104),  # UnitTypeId.DRONE,
}

race_townhalls: Dict[Race, Set[UnitTypeId]] = {
    Race.Protoss: {UnitTypeId(59)},  # UnitTypeId.NEXUS,
    Race.Terran: {
        UnitTypeId(18),  # UnitTypeId.COMMANDCENTER,
        UnitTypeId(132),  # UnitTypeId.ORBITALCOMMAND,
        UnitTypeId(130),  # UnitTypeId.PLANETARYFORTRESS,
        UnitTypeId(36),  # UnitTypeId.COMMANDCENTERFLYING,
        UnitTypeId(134),  # UnitTypeId.ORBITALCOMMANDFLYING,
    },
    Race.Zerg: {
        UnitTypeId(86),  # UnitTypeId.HATCHERY,
        UnitTypeId(100),  # UnitTypeId.LAIR,
        UnitTypeId(101),  # UnitTypeId.HIVE,
    },
    Race.Random: set(),
}
_random = []
for _race_townhalls in race_townhalls.values():
    _random += list(_race_townhalls)
race_townhalls[Race.Random] = set(_random)
del _random, _race_townhalls

warpgate_abilities: Dict[AbilityId, AbilityId] = {
    # AbilityId.GATEWAYTRAIN_ZEALOT: AbilityId.WARPGATETRAIN_ZEALOT,
    AbilityId(916): AbilityId(1413),
    # AbilityId.GATEWAYTRAIN_STALKER: AbilityId.WARPGATETRAIN_STALKER,
    AbilityId(917): AbilityId(1414),
    # AbilityId.GATEWAYTRAIN_HIGHTEMPLAR: AbilityId.WARPGATETRAIN_HIGHTEMPLAR,
    AbilityId(919): AbilityId(1416),
    # AbilityId.GATEWAYTRAIN_DARKTEMPLAR: AbilityId.WARPGATETRAIN_DARKTEMPLAR,
    AbilityId(920): AbilityId(1417),
    # AbilityId.GATEWAYTRAIN_SENTRY: AbilityId.WARPGATETRAIN_SENTRY,
    AbilityId(921): AbilityId(1418),
    # AbilityId.TRAIN_ADEPT: AbilityId.TRAINWARP_ADEPT,
    AbilityId(922): AbilityId(1419),
}

race_gas: Dict[Race, UnitTypeId] = {
    Race.Protoss: UnitTypeId(61),  # UnitTypeId.ASSIMILATOR,
    Race.Terran: UnitTypeId(20),  # UnitTypeId.REFINERY,
    Race.Zerg: UnitTypeId(88),  # UnitTypeId.EXTRACTOR,
}

# TODO fix me
transforming = {}
# transforming: Dict[UnitTypeId, AbilityId] = {
#     # Terran structures
#     BARRACKS: LAND_BARRACKS,
#     BARRACKSFLYING: LAND_BARRACKS,
#     COMMANDCENTER: LAND_COMMANDCENTER,
#     COMMANDCENTERFLYING: LAND_COMMANDCENTER,
#     ORBITALCOMMAND: LAND_ORBITALCOMMAND,
#     ORBITALCOMMANDFLYING: LAND_ORBITALCOMMAND,
#     FACTORY: LAND_FACTORY,
#     FACTORYFLYING: LAND_FACTORY,
#     STARPORT: LAND_STARPORT,
#     STARPORTFLYING: LAND_STARPORT,
#     SUPPLYDEPOT: MORPH_SUPPLYDEPOT_RAISE,
#     SUPPLYDEPOTLOWERED: MORPH_SUPPLYDEPOT_LOWER,
#     # Terran units
#     HELLION: MORPH_HELLION,
#     HELLIONTANK: MORPH_HELLBAT,
#     LIBERATOR: MORPH_LIBERATORAAMODE,
#     LIBERATORAG: MORPH_LIBERATORAGMODE,
#     SIEGETANK: UNSIEGE_UNSIEGE,
#     SIEGETANKSIEGED: SIEGEMODE_SIEGEMODE,
#     THOR: MORPH_THOREXPLOSIVEMODE,
#     THORAP: MORPH_THORHIGHIMPACTMODE,
#     VIKINGASSAULT: MORPH_VIKINGASSAULTMODE,
#     VIKINGFIGHTER: MORPH_VIKINGFIGHTERMODE,
#     WIDOWMINE: BURROWUP,
#     WIDOWMINEBURROWED: BURROWDOWN,
#     # Protoss structures
#     GATEWAY: MORPH_GATEWAY,
#     WARPGATE: MORPH_WARPGATE,
#     # Protoss units
#     OBSERVER: MORPH_OBSERVERMODE,
#     OBSERVERSIEGEMODE: MORPH_SURVEILLANCEMODE,
#     WARPPRISM: MORPH_WARPPRISMTRANSPORTMODE,
#     WARPPRISMPHASING: MORPH_WARPPRISMPHASINGMODE,
#     # Zerg structures
#     SPINECRAWLER: SPINECRAWLERROOT_SPINECRAWLERROOT,
#     SPINECRAWLERUPROOTED: SPINECRAWLERUPROOT_SPINECRAWLERUPROOT,
#     SPORECRAWLER: SPORECRAWLERROOT_SPORECRAWLERROOT,
#     SPORECRAWLERUPROOTED: SPORECRAWLERUPROOT_SPORECRAWLERUPROOT,
#     # Zerg units
#     BANELING: BURROWUP_BANELING,
#     BANELINGBURROWED: BURROWDOWN_BANELING,
#     DRONE: BURROWUP_DRONE,
#     DRONEBURROWED: BURROWDOWN_DRONE,
#     HYDRALISK: BURROWUP_HYDRALISK,
#     HYDRALISKBURROWED: BURROWDOWN_HYDRALISK,
#     INFESTOR: BURROWUP_INFESTOR,
#     INFESTORBURROWED: BURROWDOWN_INFESTOR,
#     INFESTORTERRAN: BURROWUP_INFESTORTERRAN,
#     INFESTORTERRANBURROWED: BURROWDOWN_INFESTORTERRAN,
#     LURKERMP: BURROWUP_LURKER,
#     LURKERMPBURROWED: BURROWDOWN_LURKER,
#     OVERSEER: MORPH_OVERSEERMODE,
#     OVERSEERSIEGEMODE: MORPH_OVERSIGHTMODE,
#     QUEEN: BURROWUP_QUEEN,
#     QUEENBURROWED: BURROWDOWN_QUEEN,
#     ROACH: BURROWUP_ROACH,
#     ROACHBURROWED: BURROWDOWN_ROACH,
#     SWARMHOSTBURROWEDMP: BURROWDOWN_SWARMHOST,
#     SWARMHOSTMP: BURROWUP_SWARMHOST,
#     ULTRALISK: BURROWUP_ULTRALISK,
#     ULTRALISKBURROWED: BURROWDOWN_ULTRALISK,
#     ZERGLING: BURROWUP_ZERGLING,
#     ZERGLINGBURROWED: BURROWDOWN_ZERGLING,
# }
# TODO fix me
# For now only contains units that cost supply, used in bot_ai.do()
abilityid_to_unittypeid = {}
# abilityid_to_unittypeid: Dict[AbilityId, UnitTypeId] = {
#     # Protoss
#     AbilityId.NEXUSTRAIN_PROBE: UnitTypeId.PROBE,
#     AbilityId.GATEWAYTRAIN_ZEALOT: UnitTypeId.ZEALOT,
#     AbilityId.WARPGATETRAIN_ZEALOT: UnitTypeId.ZEALOT,
#     AbilityId.TRAIN_ADEPT: UnitTypeId.ADEPT,
#     AbilityId.TRAINWARP_ADEPT: UnitTypeId.ADEPT,
#     AbilityId.GATEWAYTRAIN_STALKER: UnitTypeId.STALKER,
#     AbilityId.WARPGATETRAIN_STALKER: UnitTypeId.STALKER,
#     AbilityId.GATEWAYTRAIN_SENTRY: UnitTypeId.SENTRY,
#     AbilityId.WARPGATETRAIN_SENTRY: UnitTypeId.SENTRY,
#     AbilityId.GATEWAYTRAIN_DARKTEMPLAR: UnitTypeId.DARKTEMPLAR,
#     AbilityId.WARPGATETRAIN_DARKTEMPLAR: UnitTypeId.DARKTEMPLAR,
#     AbilityId.GATEWAYTRAIN_HIGHTEMPLAR: UnitTypeId.HIGHTEMPLAR,
#     AbilityId.WARPGATETRAIN_HIGHTEMPLAR: UnitTypeId.HIGHTEMPLAR,
#     AbilityId.ROBOTICSFACILITYTRAIN_OBSERVER: UnitTypeId.OBSERVER,
#     AbilityId.ROBOTICSFACILITYTRAIN_COLOSSUS: UnitTypeId.COLOSSUS,
#     AbilityId.ROBOTICSFACILITYTRAIN_IMMORTAL: UnitTypeId.IMMORTAL,
#     AbilityId.ROBOTICSFACILITYTRAIN_WARPPRISM: UnitTypeId.WARPPRISM,
#     AbilityId.STARGATETRAIN_CARRIER: UnitTypeId.CARRIER,
#     AbilityId.STARGATETRAIN_ORACLE: UnitTypeId.ORACLE,
#     AbilityId.STARGATETRAIN_PHOENIX: UnitTypeId.PHOENIX,
#     AbilityId.STARGATETRAIN_TEMPEST: UnitTypeId.TEMPEST,
#     AbilityId.STARGATETRAIN_VOIDRAY: UnitTypeId.VOIDRAY,
#     AbilityId.NEXUSTRAINMOTHERSHIP_MOTHERSHIP: UnitTypeId.MOTHERSHIP,
#     # Terran
#     AbilityId.COMMANDCENTERTRAIN_SCV: UnitTypeId.SCV,
#     AbilityId.BARRACKSTRAIN_MARINE: UnitTypeId.MARINE,
#     AbilityId.BARRACKSTRAIN_GHOST: UnitTypeId.GHOST,
#     AbilityId.BARRACKSTRAIN_MARAUDER: UnitTypeId.MARAUDER,
#     AbilityId.BARRACKSTRAIN_REAPER: UnitTypeId.REAPER,
#     AbilityId.FACTORYTRAIN_HELLION: UnitTypeId.HELLION,
#     AbilityId.FACTORYTRAIN_SIEGETANK: UnitTypeId.SIEGETANK,
#     AbilityId.FACTORYTRAIN_THOR: UnitTypeId.THOR,
#     AbilityId.FACTORYTRAIN_WIDOWMINE: UnitTypeId.WIDOWMINE,
#     AbilityId.TRAIN_HELLBAT: UnitTypeId.HELLIONTANK,
#     AbilityId.TRAIN_CYCLONE: UnitTypeId.CYCLONE,
#     AbilityId.STARPORTTRAIN_RAVEN: UnitTypeId.RAVEN,
#     AbilityId.STARPORTTRAIN_VIKINGFIGHTER: UnitTypeId.VIKINGFIGHTER,
#     AbilityId.STARPORTTRAIN_MEDIVAC: UnitTypeId.MEDIVAC,
#     AbilityId.STARPORTTRAIN_BATTLECRUISER: UnitTypeId.BATTLECRUISER,
#     AbilityId.STARPORTTRAIN_BANSHEE: UnitTypeId.BANSHEE,
#     AbilityId.STARPORTTRAIN_LIBERATOR: UnitTypeId.LIBERATOR,
#     # Zerg
#     AbilityId.LARVATRAIN_DRONE: UnitTypeId.DRONE,
#     AbilityId.LARVATRAIN_OVERLORD: UnitTypeId.OVERLORD,
#     AbilityId.LARVATRAIN_ZERGLING: UnitTypeId.ZERGLING,
#     AbilityId.LARVATRAIN_ROACH: UnitTypeId.ROACH,
#     AbilityId.LARVATRAIN_HYDRALISK: UnitTypeId.HYDRALISK,
#     AbilityId.LARVATRAIN_MUTALISK: UnitTypeId.MUTALISK,
#     AbilityId.LARVATRAIN_CORRUPTOR: UnitTypeId.CORRUPTOR,
#     AbilityId.LARVATRAIN_ULTRALISK: UnitTypeId.ULTRALISK,
#     AbilityId.LARVATRAIN_INFESTOR: UnitTypeId.INFESTOR,
#     AbilityId.LARVATRAIN_VIPER: UnitTypeId.VIPER,
#     AbilityId.LOCUSTTRAIN_SWARMHOST: UnitTypeId.SWARMHOSTMP,
#     AbilityId.TRAINQUEEN_QUEEN: UnitTypeId.QUEEN,
# }

UNIT_BATTLECRUISER: UnitTypeId = UnitTypeId(57)  # UnitTypeId.BATTLECRUISER
UNIT_ORACLE: UnitTypeId = UnitTypeId(495)  # UnitTypeId.ORACLE
UNIT_PHOTONCANNON: UnitTypeId = UnitTypeId(66)  # UnitTypeId.PHOTONCANNON
UNIT_COLOSSUS: UnitTypeId = UnitTypeId(4)  # UnitTypeId.COLOSSUS

IS_STRUCTURE: int = Attribute.Structure.value
IS_LIGHT: int = Attribute.Light.value
IS_ARMORED: int = Attribute.Armored.value
IS_BIOLOGICAL: int = Attribute.Biological.value
IS_MECHANICAL: int = Attribute.Mechanical.value
IS_MASSIVE: int = Attribute.Massive.value
IS_PSIONIC: int = Attribute.Psionic.value
TARGET_GROUND: Set[int] = {TargetType.Ground.value, TargetType.Any.value}
TARGET_AIR: Set[int] = {TargetType.Air.value, TargetType.Any.value}
TARGET_BOTH = TARGET_GROUND | TARGET_AIR
IS_SNAPSHOT = DisplayType.Snapshot.value
IS_VISIBLE = DisplayType.Visible.value
IS_MINE = Alliance.Self.value
IS_ENEMY = Alliance.Enemy.value
IS_CLOAKED: Set[int] = {CloakState.Cloaked.value, CloakState.CloakedDetected.value, CloakState.CloakedAllied.value}
IS_REVEALED: Set[int] = CloakState.CloakedDetected.value
CAN_BE_ATTACKED: Set[int] = {CloakState.NotCloaked.value, CloakState.CloakedDetected.value}
IS_CARRYING_MINERALS: Set[BuffId] = {
    BuffId(271),
    BuffId(272),
}  # {BuffId.CARRYMINERALFIELDMINERALS, BuffId.CARRYHIGHYIELDMINERALFIELDMINERALS}
IS_CARRYING_VESPENE: Set[BuffId] = {
    BuffId(273),  # BuffId.CARRYHARVESTABLEVESPENEGEYSERGAS,
    BuffId(274),  # BuffId.CARRYHARVESTABLEVESPENEGEYSERGASPROTOSS,
    BuffId(275),  # BuffId.CARRYHARVESTABLEVESPENEGEYSERGASZERG,
}
IS_CARRYING_RESOURCES: Set[BuffId] = IS_CARRYING_MINERALS | IS_CARRYING_VESPENE
IS_ATTACKING: Set[AbilityId] = {
    AbilityId(3674),  # AbilityId.ATTACK,
    AbilityId(23),  # AbilityId.ATTACK_ATTACK,
    AbilityId(24),  # AbilityId.ATTACK_ATTACKTOWARDS,
    AbilityId(25),  # AbilityId.ATTACK_ATTACKBARRAGE,
    AbilityId(19),  # AbilityId.SCAN_MOVE,
}
IS_PATROLLING: AbilityId = AbilityId(17)  # AbilityId.PATROL_PATROL
IS_GATHERING: AbilityId = AbilityId(3666)  # AbilityId.HARVEST_GATHER
IS_RETURNING: AbilityId = AbilityId(3667)  # AbilityId.HARVEST_RETURN
IS_COLLECTING: Set[AbilityId] = {IS_GATHERING, IS_RETURNING}
IS_CONSTRUCTING_SCV: Set[AbilityId] = {
    AbilityId(331),  # AbilityId.TERRANBUILD_ARMORY,
    AbilityId(321),  # AbilityId.TERRANBUILD_BARRACKS,
    AbilityId(324),  # AbilityId.TERRANBUILD_BUNKER,
    AbilityId(318),  # AbilityId.TERRANBUILD_COMMANDCENTER,
    AbilityId(322),  # AbilityId.TERRANBUILD_ENGINEERINGBAY,
    AbilityId(328),  # AbilityId.TERRANBUILD_FACTORY,
    AbilityId(333),  # AbilityId.TERRANBUILD_FUSIONCORE,
    AbilityId(327),  # AbilityId.TERRANBUILD_GHOSTACADEMY,
    AbilityId(323),  # AbilityId.TERRANBUILD_MISSILETURRET,
    AbilityId(320),  # AbilityId.TERRANBUILD_REFINERY,
    AbilityId(326),  # AbilityId.TERRANBUILD_SENSORTOWER,
    AbilityId(329),  # AbilityId.TERRANBUILD_STARPORT,
    AbilityId(319),  # AbilityId.TERRANBUILD_SUPPLYDEPOT,
}
IS_REPAIRING: Set[AbilityId] = {
    AbilityId(3685),
    AbilityId(78),
    AbilityId(316),
}  # {AbilityId.EFFECT_REPAIR, AbilityId.EFFECT_REPAIR_MULE, AbilityId.EFFECT_REPAIR_SCV}
IS_DETECTOR: Set[UnitTypeId] = {
    UnitTypeId(82),  # UnitTypeId.OBSERVER,
    UnitTypeId(1911),  # UnitTypeId.OBSERVERSIEGEMODE,
    UnitTypeId(56),  # UnitTypeId.RAVEN,
    UnitTypeId(23),  # UnitTypeId.MISSILETURRET,
    UnitTypeId(129),  # UnitTypeId.OVERSEER,
    UnitTypeId(1912),  # UnitTypeId.OVERSEERSIEGEMODE,
    UnitTypeId(99),  # UnitTypeId.SPORECRAWLER,
}

ABILITY_ATTACK: AbilityId = AbilityId(23)
ABILITY_SMART: AbilityId = AbilityId(1)
ABILITY_GATHER: AbilityId = AbilityId(3666)
ABILITY_RETURN: AbilityId = AbilityId(3667)
ABILITY_MOVE: AbilityId = AbilityId(16)
ABILITY_HOLDPOSITION: AbilityId = AbilityId(18)
ABILITY_STOP: AbilityId = AbilityId(4)
ABILITY_PATROL: AbilityId = AbilityId(17)
ABILITY_REPAIR: AbilityId = AbilityId(3685)

SPEED_UPGRADE_DICT: Dict[UnitTypeId, UpgradeId] = {
    # Terran
    UnitTypeId(54): UpgradeId(137),  # UnitTypeId.MEDIVAC: UpgradeId.MEDIVACRAPIDDEPLOYMENT,
    UnitTypeId(55): UpgradeId(136),  # UnitTypeId.BANSHEE: UpgradeId.BANSHEESPEED,
    # Protoss
    UnitTypeId(73): UpgradeId(86),  # UnitTypeId.ZEALOT: UpgradeId.CHARGE,
    UnitTypeId(82): UpgradeId(48),  # UnitTypeId.OBSERVER: UpgradeId.OBSERVERGRAVITICBOOSTER,
    UnitTypeId(81): UpgradeId(49),  # UnitTypeId.WARPPRISM: UpgradeId.GRAVITICDRIVE,
    UnitTypeId(80): UpgradeId(288),  # UnitTypeId.VOIDRAY: UpgradeId.VOIDRAYSPEEDUPGRADE,
    # Zerg
    UnitTypeId(106): UpgradeId(62),  # UnitTypeId.OVERLORD: UpgradeId.OVERLORDSPEED,
    UnitTypeId(129): UpgradeId(62),  # UnitTypeId.OVERSEER: UpgradeId.OVERLORDSPEED,
    UnitTypeId(105): UpgradeId(66),  # UnitTypeId.ZERGLING: UpgradeId.ZERGLINGMOVEMENTSPEED,
    UnitTypeId(9): UpgradeId(75),  # UnitTypeId.BANELING: UpgradeId.CENTRIFICALHOOKS,
    UnitTypeId(110): UpgradeId(2),  # UnitTypeId.ROACH: UpgradeId.GLIALRECONSTITUTION,
    UnitTypeId(502): UpgradeId(293),  # UnitTypeId.LURKERMP: UpgradeId.DIGGINGCLAWS,
}
SPEED_INCREASE_DICT: Dict[UnitTypeId, float] = {
    # Terran
    UnitTypeId.MEDIVAC: 1.18,
    UnitTypeId.BANSHEE: 1.3636,
    # Protoss
    UnitTypeId.ZEALOT: 1.5,
    UnitTypeId.OBSERVER: 2,
    UnitTypeId.WARPPRISM: 1.3,
    UnitTypeId.VOIDRAY: 1.328,
    # Zerg
    UnitTypeId.OVERLORD: 2.915,
    UnitTypeId.OVERSEER: 1.8015,
    UnitTypeId.ZERGLING: 1.6,
    UnitTypeId.BANELING: 1.18,
    UnitTypeId.ROACH: 1.3333333333,
    UnitTypeId.LURKERMP: 1.1,
}
temp1 = set(SPEED_UPGRADE_DICT.keys())
temp2 = set(SPEED_INCREASE_DICT.keys())
assert temp1 == temp2, f"{temp1.symmetric_difference(temp2)}"
del temp1
del temp2
SPEED_INCREASE_ON_CREEP_DICT: Dict[UnitTypeId, float] = {
    UnitTypeId.QUEEN: 2.67,
    UnitTypeId.ZERGLING: 1.3,
    UnitTypeId.BANELING: 1.3,
    UnitTypeId.ROACH: 1.3,
    UnitTypeId.RAVAGER: 1.3,
    UnitTypeId.HYDRALISK: 1.3,
    UnitTypeId.LURKERMP: 1.3,
    UnitTypeId.ULTRALISK: 1.3,
    UnitTypeId.INFESTOR: 1.3,
    UnitTypeId.INFESTORTERRAN: 1.3,
    UnitTypeId.SWARMHOSTMP: 1.3,
    UnitTypeId.LOCUSTMP: 1.4,
    UnitTypeId.SPINECRAWLER: 2.5,
    UnitTypeId.SPORECRAWLER: 2.5,
}
OFF_CREEP_SPEED_UPGRADE_DICT: Dict[UnitTypeId, UpgradeId] = {
    UnitTypeId.HYDRALISK: UpgradeId.EVOLVEMUSCULARAUGMENTS,
    UnitTypeId.ULTRALISK: UpgradeId.ANABOLICSYNTHESIS,
}
OFF_CREEP_SPEED_INCREASE_DICT: Dict[UnitTypeId, float] = {
    UnitTypeId.HYDRALISK: 1.25,
    UnitTypeId.ULTRALISK: 1.2,
}
temp1 = set(OFF_CREEP_SPEED_UPGRADE_DICT.keys())
temp2 = set(OFF_CREEP_SPEED_INCREASE_DICT.keys())
assert temp1 == temp2, f"{temp1.symmetric_difference(temp2)}"
del temp1
del temp2
# Movement speed gets altered by this factor if it is affected by this buff
# TODO fix me
SPEED_ALTERING_BUFFS = {}
# SPEED_ALTERING_BUFFS: Dict[BuffId, float] = {
#     # Stimpack increases speed by 1.5
#     BuffId.STIMPACK: 1.5,
#     BuffId.STIMPACKMARAUDER: 1.5,
#     BuffId.CHARGEUP: 2.2,  # x2.8 speed up in pre version 4.11
#     # Concussive shells of Marauder reduce speed by 50%
#     BuffId.DUTCHMARAUDERSLOW: 0.5,
#     # Time Warp of Mothership reduces speed by 50%
#     BuffId.TIMEWARPPRODUCTION: 0.5,
#     # Fungal Growth of Infestor reduces speed by 75%
#     BuffId.FUNGALGROWTH: 0.25,
#     # Inhibitor Zones reduce speed by 35%
#     BuffId.INHIBITORZONETEMPORALFIELD: 0.65,
#     # TODO there is a new zone coming (acceleration zone) which increase movement speed, ultralisk will be affected by this
# }

TERRAN_STRUCTURES_REQUIRE_SCV: Set[UnitTypeId] = {
    UnitTypeId.ARMORY,
    UnitTypeId.BARRACKS,
    UnitTypeId.BUNKER,
    UnitTypeId.COMMANDCENTER,
    UnitTypeId.ENGINEERINGBAY,
    UnitTypeId.FACTORY,
    UnitTypeId.FUSIONCORE,
    UnitTypeId.GHOSTACADEMY,
    UnitTypeId.MISSILETURRET,
    UnitTypeId.REFINERY,
    UnitTypeId.STARPORT,
    UnitTypeId.SUPPLYDEPOT,
}
# Add REFINERYRICH if this game version supports it
try:
    TERRAN_STRUCTURES_REQUIRE_SCV.add(UnitTypeId(1943))
except ValueError:
    pass


def return_NOTAUNIT():
    # NOTAUNIT = 0
    return NOTAUNIT


# Hotfix for structures and units as the API does not seem to return the correct values, e.g. ghost and thor have None in the requirements
# TODO fix me
TERRAN_TECH_REQUIREMENT = {}
# TERRAN_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
#     return_NOTAUNIT,
#     {
#         MISSILETURRET: ENGINEERINGBAY,
#         SENSORTOWER: ENGINEERINGBAY,
#         PLANETARYFORTRESS: ENGINEERINGBAY,
#         BARRACKS: SUPPLYDEPOT,
#         ORBITALCOMMAND: BARRACKS,
#         BUNKER: BARRACKS,
#         GHOST: GHOSTACADEMY,
#         GHOSTACADEMY: BARRACKS,
#         FACTORY: BARRACKS,
#         ARMORY: FACTORY,
#         HELLIONTANK: ARMORY,
#         THOR: ARMORY,
#         STARPORT: FACTORY,
#         FUSIONCORE: STARPORT,
#         BATTLECRUISER: FUSIONCORE,
#     },
# )
PROTOSS_TECH_REQUIREMENT = {}
# PROTOSS_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
#     return_NOTAUNIT,
#     {
#         PHOTONCANNON: FORGE,
#         CYBERNETICSCORE: GATEWAY,
#         SENTRY: CYBERNETICSCORE,
#         STALKER: CYBERNETICSCORE,
#         ADEPT: CYBERNETICSCORE,
#         TWILIGHTCOUNCIL: CYBERNETICSCORE,
#         SHIELDBATTERY: CYBERNETICSCORE,
#         TEMPLARARCHIVE: TWILIGHTCOUNCIL,
#         DARKSHRINE: TWILIGHTCOUNCIL,
#         HIGHTEMPLAR: TEMPLARARCHIVE,
#         DARKTEMPLAR: DARKSHRINE,
#         STARGATE: CYBERNETICSCORE,
#         TEMPEST: FLEETBEACON,
#         CARRIER: FLEETBEACON,
#         MOTHERSHIP: FLEETBEACON,
#         ROBOTICSFACILITY: CYBERNETICSCORE,
#         ROBOTICSBAY: ROBOTICSFACILITY,
#         COLOSSUS: ROBOTICSBAY,
#         DISRUPTOR: ROBOTICSBAY,
#     },
# )
ZERG_TECH_REQUIREMENT = {}
# ZERG_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
#     return_NOTAUNIT,
#     {
#         ZERGLING: SPAWNINGPOOL,
#         QUEEN: SPAWNINGPOOL,
#         ROACHWARREN: SPAWNINGPOOL,
#         BANELINGNEST: SPAWNINGPOOL,
#         SPINECRAWLER: SPAWNINGPOOL,
#         SPORECRAWLER: SPAWNINGPOOL,
#         ROACH: ROACHWARREN,
#         BANELING: BANELINGNEST,
#         LAIR: SPAWNINGPOOL,
#         OVERSEER: LAIR,
#         OVERLORDTRANSPORT: LAIR,
#         INFESTATIONPIT: LAIR,
#         INFESTOR: INFESTATIONPIT,
#         SWARMHOSTMP: INFESTATIONPIT,
#         HYDRALISKDEN: LAIR,
#         HYDRALISK: HYDRALISKDEN,
#         LURKERDENMP: HYDRALISKDEN,
#         LURKERMP: LURKERDENMP,
#         SPIRE: LAIR,
#         MUTALISK: SPIRE,
#         CORRUPTOR: SPIRE,
#         NYDUSNETWORK: LAIR,
#         HIVE: INFESTATIONPIT,
#         VIPER: HIVE,
#         ULTRALISKCAVERN: HIVE,
#         GREATERSPIRE: HIVE,
#         BROODLORD: GREATERSPIRE,
#     },
# )
# Required in 'tech_requirement_progress' bot_ai.py function
EQUIVALENTS_FOR_TECH_PROGRESS: Dict[UnitTypeId, Set[UnitTypeId]] = {
    UnitTypeId.SUPPLYDEPOT: {UnitTypeId.SUPPLYDEPOTLOWERED},
    UnitTypeId.BARRACKS: {UnitTypeId.BARRACKSFLYING},
    UnitTypeId.FACTORY: {UnitTypeId.FACTORYFLYING},
    UnitTypeId.STARPORT: {UnitTypeId.STARPORTFLYING},
    UnitTypeId.COMMANDCENTER: {
        UnitTypeId.COMMANDCENTERFLYING,
        UnitTypeId.PLANETARYFORTRESS,
        UnitTypeId.ORBITALCOMMAND,
        UnitTypeId.ORBITALCOMMANDFLYING,
    },
    UnitTypeId.LAIR: {UnitTypeId.HIVE},
    UnitTypeId.HATCHERY: {UnitTypeId.LAIR, UnitTypeId.HIVE},
    UnitTypeId.SPIRE: {UnitTypeId.GREATERSPIRE},
}
ALL_GAS: Set[UnitTypeId] = {
    UnitTypeId.ASSIMILATOR,
    # UnitTypeId.ASSIMILATORRICH,
    UnitTypeId.REFINERY,
    # UnitTypeId.REFINERYRICH,
    UnitTypeId.EXTRACTOR,
    # UnitTypeId.EXTRACTORRICH,
}
# Add rich gas if current game version allows it
try:
    ALL_GAS.update({
        UnitTypeId(1943),
        UnitTypeId(1980),
        UnitTypeId(1981),
    })
except ValueError:
    pass
"""
How much damage a unit gains per weapon upgrade per attack
E.g. marauder receives +1 normal damage and +1 vs armored, so we have to list +1 vs armored here - the +1 normal damage is assumed
E.g. stalker receives +1 normal damage but does not increment at all vs armored, so we don't list it here
Updated using unit stats: https://liquipedia.net/starcraft2/Unit_Statistics_(Legacy_of_the_Void)

Default will be assumed as 1, or 0 against specific armor tags, if it is not listed:
MyUnitType: {
    TargetType.Ground.value: {
        # Bonus damage per weapon upgrade against ground targets
        None: 1,
        # Bonus damage per weapon upgrade against ground targets with specific armor tag
        some_armor_tag: 0
    }
    # Same for Air and Any (=both)
}    
"""
DAMAGE_BONUS_PER_UPGRADE: Dict[int, UnitTypeId] = {
    #
    # Protoss
    #
    UnitTypeId.PROBE: {TargetType.Ground.value: {None: 0}},
    # Gateway Units
    UnitTypeId.ADEPT: {TargetType.Ground.value: {IS_LIGHT: 1}},
    UnitTypeId.STALKER: {TargetType.Any.value: {IS_ARMORED: 1}},
    UnitTypeId.DARKTEMPLAR: {TargetType.Ground.value: {None: 5}},
    UnitTypeId.ARCHON: {TargetType.Any.value: {None: 3, IS_BIOLOGICAL: 1}},
    # Robo Units
    UnitTypeId.IMMORTAL: {TargetType.Ground.value: {None: 2, IS_ARMORED: 3}},
    UnitTypeId.COLOSSUS: {TargetType.Ground.value: {IS_LIGHT: 1}},
    # Stargate Units
    UnitTypeId.ORACLE: {TargetType.Ground.value: {None: 0}},
    UnitTypeId.TEMPEST: {TargetType.Ground.value: {None: 4}, TargetType.Air.value: {None: 3, IS_MASSIVE: 2}},
    #
    # Terran
    #
    UnitTypeId.SCV: {TargetType.Ground.value: {None: 0}},
    # Barracks Units
    UnitTypeId.MARAUDER: {TargetType.Ground.value: {IS_ARMORED: 1}},
    UnitTypeId.GHOST: {TargetType.Any.value: {IS_LIGHT: 1}},
    # Factory Units
    UnitTypeId.HELLION: {TargetType.Ground.value: {IS_LIGHT: 1}},
    UnitTypeId.HELLIONTANK: {TargetType.Ground.value: {None: 2, IS_LIGHT: 1}},
    UnitTypeId.CYCLONE: {TargetType.Any.value: {None: 2}},
    UnitTypeId.SIEGETANK: {TargetType.Ground.value: {None: 2, IS_ARMORED: 1}},
    UnitTypeId.SIEGETANKSIEGED: {TargetType.Ground.value: {None: 4, IS_ARMORED: 1}},
    UnitTypeId.THOR: {TargetType.Ground.value: {None: 3}, TargetType.Air.value: {IS_LIGHT: 1}},
    UnitTypeId.THORAP: {TargetType.Ground.value: {None: 3}, TargetType.Air.value: {None: 3, IS_MASSIVE: 1}},
    # Starport Units
    UnitTypeId.VIKINGASSAULT: {TargetType.Ground.value: {IS_MECHANICAL: 1}},
    UnitTypeId.LIBERATORAG: {TargetType.Ground.value: {None: 5}},
    #
    # Zerg
    #
    UnitTypeId.DRONE: {TargetType.Ground.value: {None: 0}},
    # Hatch Tech Units (Queen, Ling, Bane, Roach, Ravager)
    UnitTypeId.BANELING: {TargetType.Ground.value: {None: 2, IS_LIGHT: 2, IS_STRUCTURE: 3}},
    UnitTypeId.ROACH: {TargetType.Ground.value: {None: 2}},
    UnitTypeId.RAVAGER: {TargetType.Ground.value: {None: 2}},
    # Lair Tech Units (Hydra, Lurker, Ultra)
    UnitTypeId.LURKERMPBURROWED: {TargetType.Ground.value: {None: 2, IS_ARMORED: 1}},
    UnitTypeId.ULTRALISK: {TargetType.Ground.value: {None: 3}},
    # Spire Units (Muta, Corruptor, BL)
    UnitTypeId.CORRUPTOR: {TargetType.Air.value: {IS_MASSIVE: 1}},
    UnitTypeId.BROODLORD: {TargetType.Ground.value: {None: 2}},
}
