import telebot
from telebot import types
import sqlite3
import os

######################################################

bot = telebot.TeleBot('6401641976:AAGJ79i5DjEyqzZyVZ-wL5qwsmyVNPr7E4E')

nickname = ''
password = ''
energy = 0
time_out = 1
build = ''
buildes = ''
users = ''
mark_us = 0
mark_us_new = 0
na_au = ''
title_build_user1 = ''


######################################################


all_info_game = {
    'classes': ['hunter', 'titan', 'warlock'],
    'element': ['ark', 'solar', 'stasis', 'strand', 'void'],
    'super.ability': {
        'warlock': {
            'solar': ['Daybreak', 'Well Of Radiance'],
            'ark': ['Chaos Reach', 'Stormtrance'],
            'void': ['Nova Bomb - Catacysm', 'Nova Bomb - Vortex', 'Nova Warp'],
            'stasis': ["Winter's Wrath"],
            'strand': ['Needlestorm']
        },
        'titan': {
            'solar': ['Burning Maul', 'Hammer of Sol'],
            'ark': ['Fists of Havoc', 'Thundercrash'],
            'void': ['Sentinel Shield', 'Ward of Dawn'],
            'stasis': ['none'],
            'strand': ['none']
        },
        'hunter': {
            'solar': ['Blade Barrage', 'Golden Gun - Deadshot', 'Golden Gun - Marksman'],
            'ark': ['Ark Staff', 'Gathering Storm'],
            'void': ['Shadowshot: Deadfall', 'Shadowshot: Moebius Quiver', 'Spectral Blades'],
            'stasis': ['Silence and Squall'],
            'strand': ['Silkstrike']
        }
    },
    'ability': {
        'warlock': {
            'solar': {
                'rift': ['empovering rift', 'healing rift', 'phoenix dive'],
                'glide': ['balanced glide', 'burst glide', 'strafe glide'],
                'melee': ['celestial fire', 'incinerator snap'],
                'grenade': ['firebolt grenade', 'fusion grenade', 'healing grenade', 'incendiary grenade', 'solar grenade', 'swarm grenade', 'thermite grenade', 'tripmine grenade']
            },
            'ark': {
                'rift': ['empovering rift', 'healing rift'],
                'glide': ['balanced glide', 'burst glide', 'strafe glide'],
                'melee': ['ball lightning', 'chain lightning'],
                'grenade': ['arcbolt grenade', 'flashbang grenade', 'flux grenade', 'lightning grenade', 'pulse grenade', 'skip grenade', 'storm grenade']
            },
            'void': {
                'rift': ['empovering rift', 'healing rift'],
                'glide': ['balanced glide', 'blink', 'burst glide', 'strafe glide'],
                'melee': ['pocket singularity'],
                'grenade': ['axion bolt', 'magnetic grenade', 'scatter grenade', 'suppressor grenade', 'void spike', 'void wall', 'vortex grenade']
            },
            'stasis': {
                'rift': ['empovering rift', 'healing rift'],
                'glide': ['balanced glide', 'burst glide', 'strafe glide'],
                'melee': ['penumbral blast'],
                'grenade': ['coldsnap grenade', 'duskfield grenade', 'glacier grenade']
            },
            'strand': {
                'rift': ['empovering rift', 'healing rift'],
                'glide': ['balanced glide', 'burst glide', 'strafe glide'],
                'melee': ['arkane needle'],
                'grenade': ['grapple', 'shackle grenade', 'threadling grenade']
            }
        },
        'titan': {
            'solar': {
                'barricade': ['towering barricade', 'rally barricade'],
                'lift': ['catapult lift', 'high lift', 'strafe lift'],
                'melee': ['hammer strike', 'throwing hammer'],
                'grenade': ['firebolt grenade', 'fusion grenade', 'healing grenade', 'incendiary grenade', 'solar grenade', 'swarm grenade', 'thermite grenade', 'tripmine grenade']
            },
            'ark': {
                'barricade': ['thruster', 'towering barricade', 'rally barricade'],
                'lift': ['catapult lift', 'high lift', 'strafe lift'],
                'melee': ['ballistic slam', 'seismic strike', 'thunderclap'],
                'grenade': ['arcbolt grenade', 'flashbang grenade', 'flux grenade', 'lightning grenade', 'pulse grenade', 'skip grenade', 'storm grenade']
            },
            'void': {
                'barricade': ['towering barricade', 'rally barricade'],
                'lift': ['catapult lift', 'high lift', 'strafe lift'],
                'melee': ['shield bash', 'shield throw'],
                'grenade': ['axion bolt', 'magnetic grenade', 'scatter grenade', 'suppressor grenade', 'void spike', 'void wall', 'vortex grenade']
            },
            'stasis': {
                'barricade': ['none'],
                'lift': ['none'],
                'melee': ['none'],
                'grenade': ['coldsnap grenade', 'duskfield grenade', 'glacier grenade']
            },
            'strand': {
                'barricade': ['none'],
                'lift': ['none'],
                'melee': ['none'],
                'grenade': ['grapple', 'shackle grenade', 'threadling grenade']
            }
        },
        'hunter': {
            'solar': {
                'dodge': ["arobat's dodge", "gambler's dodge", "marksman's dodge"],
                'jump': ['high jump', 'strafe jump', 'triple jump'],
                'melee': ['knife trick', 'lightweight knife', 'proximity explosive knife', 'weighted throwing knife'],
                'grenade': ['firebolt grenade', 'fusion grenade', 'healing grenade', 'incendiary grenade', 'solar grenade', 'swarm grenade', 'thermite grenade', 'tripmine grenade']
            },
            'ark': {
                'dodge': ["gambler's dodge", "marksman's dodge"],
                'jump': ['blink', 'high jump', 'strafe jump', 'triple jump'],
                'melee': ['combination blow', 'disorienting blow'],
                'grenade': ['arcbolt grenade', 'flashbang grenade', 'flux grenade', 'lightning grenade', 'pulse grenade', 'skip grenade', 'storm grenade']
            },
            'void': {
                'dodge': ["gambler's dodge", "marksman's dodge"],
                'jump': ['high jump', 'strafe jump', 'triple jump'],
                'melee': ['snare bomb'],
                'grenade': ['axion bolt', 'magnetic grenade', 'scatter grenade', 'suppressor grenade', 'void spike', 'void wall', 'vortex grenade']
            },
            'stasis': {
                'dodge': ["gambler's dodge", "marksman's dodge"],
                'jump': ['high jump', 'strafe jump', 'triple jump'],
                'melee': ['withering blade'],
                'grenade': ['coldsnap grenade', 'duskfield grenade', 'glacier grenade']
            },
            'strand': {
                'dodge': ["gambler's dodge", "marksman's dodge"],
                'jump': ['high jump', 'strafe jump', 'triple jump'],
                'melee': ['threaded spike'],
                'grenade': ['grapple', 'shackle grenade', 'threadling grenade']
            }
        }
    },
    'artefacts': {
        'warlock': {
            'solar': ['Heat Rises', 'Icarus Dash', 'Touch of Flame'],
            'ark': ['Arc Soul', 'Electrostatic Mind', 'Lightning Surge'],
            'void': ['Chaos Accelerant', 'Child of the Old Gods', 'Feed the Void'],
            'stasis': ['Bleak Watcher', 'Frostpulse', 'Glacial Harwest', 'Iceflare Bolts'],
            'strand': ['Mindspun Invocation', 'Ihe Wanderer', "Weaver's Call", 'Weavewalk']
        },
        'titan': {
            'solar': ['Consecration', 'Roaring Flames', 'Sol Invictus'],
            'ark': ['Juggernaut', 'Knockout', 'Touch of Thunder'],
            'void': ['Bastion', 'Controlled Demolition', 'Offensive Bulwark'],
            'stasis': ['none'],
            'strand': ['none']
        },
        'hunter': {
            'solar': ['Gunpowder Gamble', "Knock 'em Down", 'On Your Mark'],
            'ark': ['Flow State', 'Lethal Current', 'Tempest Strike'],
            'void': ['Stylish Executioner', "Trapper's Ambush", 'Vanishing Step'],
            'stasis': ['Grim Harvest', 'Shatterdive', 'Touch of Winter', "Winter's Shroud"],
            'strand': ['Ensnaring Slam', 'Threaded Specter', 'Whirling Maelstrom', "Widow's Silk"]
        }
    },
    'modification.ability': {
        'warlock': {
            'solar': ['Ember of Ashes', 'Ember of Beams', 'Ember of Benevolence', 'Ember of Blistering', 'Ember of Char', 'Ember of Combustion', 'Ember of Empyrean', 'Ember of Eruption', 'Ember of Mercy', 'Ember of Resolve', 'Ember of Searing', 'Ember of Singeing', 'Ember of Solace', 'Ember of Tempering', 'Ember of Torches', 'Ember of Wonder'],
            'ark': ['Spark of Amplitude', 'Spark of Beacons', 'Spark of Brilliance', 'Spark of Discharge', 'Spark of Feedback', 'Spark of Focus', 'Spark of Frequency', 'Spark of Haste', 'Spark of Instinct', 'Spark of Ions', 'Spark of Magnitude', 'Spark of Momentum', 'Spark of Recharge', 'Spark of Resistance', 'Spark of Shock', 'Spark of Volts'],
            'void': ['Echo of Cessation', 'Echo of Dilation', 'Echo of Domineering', 'Echo of Exchange', 'Echo of Expulsion', 'Echo of Harvest', 'Echo of Instability', 'Echo of Leeching', 'Echo of Obscurity', 'Echo of Persistence', 'Echo of Provision', 'Echo of Remnants', 'Echo of Reprisal', 'Echo of Starvation', 'Echo of Undermining', 'Echo of Vigilance'],
            'stasis': ['Whisper of Bonds', 'Whisper of Chains', 'Whisper of Conduction', 'Whisper of Durance', 'Whisper of Fissures', 'Whisper of Fractures', 'Whisper of Hedrons', 'Whisper of Hunger', 'Whisper of Impetus', 'Whisper of Refraction', 'Whisper of Rending', 'Whisper of Rime', 'Whisper of Shards', 'Whisper of Torment'],
            'strand': ['Thread of Ascent', 'Thread of Binding', 'Thread of Continuity', 'Thread of Evolution', 'Thread of Finality', 'Thread of Fury', 'Thread of Generation', 'Thread of Isolation', 'Thread of Mind', 'Thread of Propagation', 'Thread of Rebirth', 'Thread of Transmutation', 'Thread of Warding', 'Thread of Wisdom']
        },
        'titan': {
            'solar': ['Ember of Ashes', 'Ember of Beams', 'Ember of Benevolence', 'Ember of Blistering', 'Ember of Char', 'Ember of Combustion', 'Ember of Empyrean', 'Ember of Eruption', 'Ember of Mercy', 'Ember of Resolve', 'Ember of Searing', 'Ember of Singeing', 'Ember of Solace', 'Ember of Tempering', 'Ember of Torches', 'Ember of Wonder'],
            'ark': ['Spark of Amplitude', 'Spark of Beacons', 'Spark of Brilliance', 'Spark of Discharge', 'Spark of Feedback', 'Spark of Focus', 'Spark of Frequency', 'Spark of Haste', 'Spark of Instinct', 'Spark of Ions', 'Spark of Magnitude', 'Spark of Momentum', 'Spark of Recharge', 'Spark of Resistance', 'Spark of Shock', 'Spark of Volts'],
            'void': ['Echo of Cessation', 'Echo of Dilation', 'Echo of Domineering', 'Echo of Exchange', 'Echo of Expulsion', 'Echo of Harvest', 'Echo of Instability', 'Echo of Leeching', 'Echo of Obscurity', 'Echo of Persistence', 'Echo of Provision', 'Echo of Remnants', 'Echo of Reprisal', 'Echo of Starvation', 'Echo of Undermining', 'Echo of Vigilance'],
            'stasis': ['Whisper of Bonds', 'Whisper of Chains', 'Whisper of Conduction', 'Whisper of Durance', 'Whisper of Fissures', 'Whisper of Fractures', 'Whisper of Hedrons', 'Whisper of Hunger', 'Whisper of Impetus', 'Whisper of Refraction', 'Whisper of Rending', 'Whisper of Rime', 'Whisper of Shards', 'Whisper of Torment'],
            'strand': ['Thread of Ascent', 'Thread of Binding', 'Thread of Continuity', 'Thread of Evolution', 'Thread of Finality', 'Thread of Fury', 'Thread of Generation', 'Thread of Isolation', 'Thread of Mind', 'Thread of Propagation', 'Thread of Rebirth', 'Thread of Transmutation', 'Thread of Warding', 'Thread of Wisdom']
        },
        'hunter': {
            'solar': ['Ember of Ashes', 'Ember of Beams', 'Ember of Benevolence', 'Ember of Blistering', 'Ember of Char', 'Ember of Combustion', 'Ember of Empyrean', 'Ember of Eruption', 'Ember of Mercy', 'Ember of Resolve', 'Ember of Searing', 'Ember of Singeing', 'Ember of Solace', 'Ember of Tempering', 'Ember of Torches', 'Ember of Wonder'],
            'ark': ['Spark of Amplitude', 'Spark of Beacons', 'Spark of Brilliance', 'Spark of Discharge', 'Spark of Feedback', 'Spark of Focus', 'Spark of Frequency', 'Spark of Haste', 'Spark of Instinct', 'Spark of Ions', 'Spark of Magnitude', 'Spark of Momentum', 'Spark of Recharge', 'Spark of Resistance', 'Spark of Shock', 'Spark of Volts'],
            'void': ['Echo of Cessation', 'Echo of Dilation', 'Echo of Domineering', 'Echo of Exchange', 'Echo of Expulsion', 'Echo of Harvest', 'Echo of Instability', 'Echo of Leeching', 'Echo of Obscurity', 'Echo of Persistence', 'Echo of Provision', 'Echo of Remnants', 'Echo of Reprisal', 'Echo of Starvation', 'Echo of Undermining', 'Echo of Vigilance'],
            'stasis': ['Whisper of Bonds', 'Whisper of Chains', 'Whisper of Conduction', 'Whisper of Durance', 'Whisper of Fissures', 'Whisper of Fractures', 'Whisper of Hedrons', 'Whisper of Hunger', 'Whisper of Impetus', 'Whisper of Refraction', 'Whisper of Rending', 'Whisper of Rime', 'Whisper of Shards', 'Whisper of Torment'],
            'strand': ['Thread of Ascent', 'Thread of Binding', 'Thread of Continuity', 'Thread of Evolution', 'Thread of Finality', 'Thread of Fury', 'Thread of Generation', 'Thread of Isolation', 'Thread of Mind', 'Thread of Propagation', 'Thread of Rebirth', 'Thread of Transmutation', 'Thread of Warding', 'Thread of Wisdom']
        }
    },
    'exotic.armor': {
        'warlock': ['Aeon Soul', 'Apotheosis Veil', 'Astrocyte Verse', 'Ballidorse Wrathweavers', 'Boots of the Assembler', 'Briarbinds', 'Cenotaph Mask', 'Chromatic Fire', 'Claws of Ahamkara', 'Contraverse Hold', 'Crown of Tempests', 'Dawn Chorus', 'Eye of Another World', 'Fallen Sunstar', "Felwinter's Helm", 'Geomag Stabilizers', 'Getaway Artist', 'Karnstein Armlets', 'Lunafaction Boots', 'Mantle of Battle Harmony', 'Necrotic Grip', "Nezarec's Sin", 'Nothing Manacles', 'Ophidian Aspect', 'Osmiomancy Gloves', 'Phoenix Protocol', 'Promethium Spur', 'Rain of Fire', 'Sanguine Alchemy', 'Secant Filaments', 'Skull of Dire Ahamkara', 'Starfire Protocol', "Stormdancer's Brace", 'Sunbracers', 'Swarmers', 'The Stag', 'Transversive Steps', "Verity's Brow", 'Vesper of Radius', 'Wings of Sacred Dawn', "Winter's Guile"],
        'hunter': ['Aeon Swift', "Assassin's Cowl", "Athrys's Embrace", 'Blight Ranger', "Caliban's Hand", 'Celestial Nighthawk', "Cyrtarachne's Facade", 'Foetracer', 'Fr0st-EE5', 'Gemini Jester', 'Graviton Forfeit', 'Gwisin Vest', "Gyrfalcon's Hauberk", "Khepri's Sting", 'Knucklehead Radar', "Liar's Handshake", 'Lucky Pants', 'Lucky Raspberry', 'Mask of Bakris', "Mechaneer's Tricksleeves", "Mothkeeper's Wraps", 'Oathkeeper', 'Omnioculus', 'Ophidia Spathe', 'Orpheus Rig', 'Radiant Dance Machines', 'Raiden Flux', "Raiju's Harness", 'Renewal Grasps', 'Sealed Ahamkara Grasps', 'Shards of Galanor', "Shinobu's Vow", 'Speedloader Slacks', 'St0mp-EE5', 'Star-Eater Scales', 'The Bombardiers', "The Dragon's Shadow", 'The Sixth Coyote', 'Triton Vice', 'Wormhusk Crown', "Young Ahamkara's Spine"],
        'titan': ['ACD-0 Feedback Fence', 'Abeyant Leap', 'Actium War Rig', 'Aeon Safe', 'An Insurmountable Skullfort', 'Antaeus Wards', 'Arbor Warden', 'Armamentarium', 'Ashen Wake', 'Cadmus Ridge Lancecap', "Citan's Ramparts", 'Crest of Alpha Lupi', 'Cuirass of the Falling Star', 'Doom Fang Pauldron', 'Dunemarchers', 'Eternal Warrior', 'Hallowfire Heart', 'Heart of Inmost Light', 'Helm of Saint-14', 'Hoarfrost-Z', 'Icefall Mantle', "Khepri's Horn", 'Lion Rampant', 'Loreley Splendor Helm', 'Mask of the Quiet One', 'Mk. 44 Stand Asides', 'No Backup Plans', 'One-Eyed Mask', 'Peacekeepers', 'Peregrine Greaves', 'Phoenix Cradle', 'Point-Contact Cannon Brace', 'Precious Scars', 'Pyrogale Gauntlets', 'Second Chance', 'Severance Enclosure', 'Stronghold', 'Synthoceps', 'The Path of Burning Steps', 'Ursa Furiosa', 'Wormgod Caress']
    },
    'exotic.weapons': {
        'kinetic': ['Ace of Spades', "Ager's Scepter", 'Arbalest', 'Bad Juju', 'Bastion_', 'Cerberus+1', 'Conditional Finality', 'Crimson', 'Cryosthesia 77K', "Dead Man's Tale", 'Final Warning', 'Forerunner', 'Hawkmoon', "Izanagi's Burden", 'Lumina', 'MIDA Multi-Tool', 'Malfeasance', 'Monte Carlo', 'Necrochasm', 'No Time to Explain', 'Osteo Striga', 'Outbreak Perfected', 'Quicksilver Storm', 'Rat King', 'Revision Zero', 'SUROS Regime', 'Sturm', 'Sweet Business', 'The Chaperone', 'The Huckleberry', 'The Jade Rabbit', 'The Last Word', 'The Navigator', 'Thorn', 'Touch of Malice', "Traveler's Chosen", 'Verglas Curve', 'Vigilance Wing', 'Wish-Ender', 'Wish-Keeper', 'Witherhoard'],
        'energy': ['Borealis', 'Centrifuse', 'Cloudstrike', 'Coldheart', 'Collective Obligation', 'Dead Messenger', 'Delicate Tomb', "Devil's Ruin", 'Divinity', 'Duality', 'Edge of Action', 'Edge of Concurrence', 'Edge of Intent', "Eriana's Vow", 'Ex Diris', 'Fighting Lion', 'Graviton Lance', 'Hard Light', 'Hierarchy of Needs', 'Jötunn', 'Le Monarque', 'Lord of Wolves', 'Lorentz Driver', 'Merciless', 'Polaris Lance', 'Prometheus Lens', 'Riskrunner', 'Ruinous Effigy', "Skyburner's Oath", 'Sunshot', 'Symmetry', 'Tarrabah', 'Telesto', 'Tessellation', 'The Fourth Horseman', 'The Manticore', "Ticuu's Divination", "Tommy's Matchbook", 'Trespasser', 'Trinity Ghoul', 'Vex Mythoclast', 'Vexcalibur', 'Wavesplitter'],
        'power': ['Anarchy', 'Black Talon', 'D.A.R.C.I.', 'Deathbringer', 'Deterministic Chaos', "Dragon's Breath", 'Eyes of Tomorrow', 'Gjallarhorn', 'Grand Overture', 'Heartshadow', 'Heir Apparent', "Legend of Acrius", "Leviathan's Breath", 'One Thousand Voices', 'Parasite', "Salvation's Grip", 'Sleeper Simulant', 'The Colony', 'The Lament', 'The Prospector', 'The Queenbreaker', 'The Wardcliff Coil', 'Thunderlord', 'Tractor Cannon', 'Truth', 'Two-Tailed Fox', 'Whisper of the Worm', 'Winterbite', 'Worldline Zero', 'Xenophage']
    },
    'legendary.weapons': {
        'kinetic': ['BrayTech Werewolf (Auto Rifle)', 'BrayTech Winter Wolf (Auto Rifle)', 'Breakneck (Auto Rifle)', 'Chroma Rush (Auto Rifle)', 'Duty Bound (Auto Rifle)', 'Duty Bound (Adept) (Auto Rifle)', 'Ether Doctor (Auto Rifle)', 'False Promises (Auto Rifle)', 'Firefright (Auto Rifle)', 'Foregone Conclusion (Auto Rifle)', "Gahlran's Right Hand (Auto Rifle)", 'Ghost Primus (Auto Rifle)', 'Guiding Star (Auto Rifle)', 'Halfdan-D (Auto Rifle)', 'Hazard of the Cast (Auto Rifle)', 'Herod-C (Auto Rifle)', 'Horror Story (Auto Rifle)', 'Krait (Auto Rifle)', 'Lodbrok-C (Auto Rifle)', 'Loquitor IV (Auto Rifle)', 'Old Sterling (Auto Rifle)', 'Origin Story (Auto Rifle)', "Orimund's Anvil (Auto Rifle)", 'Perpetualis (Auto Rifle)', 'Pluperfect (Auto Rifle)', "Rufus's Fury (Auto Rifle)", "Rufus's Fury (Adept) (Auto Rifle)", 'Scathelocke (Auto Rifle)', 'Seventh Seraph Carbine (Auto Rifle)', 'Steelfeather Repeater (Auto Rifle)', 'The Doubt (Auto Rifle)', 'The Forward Path (Auto Rifle)', 'The Last Breath (Auto Rifle)', 'Tigerspite (Auto Rifle)', 'Accrued Redemption (Combat Bow)', 'Biting Winds (Combat Bow)', 'Fel Taradiddle (Combat Bow)', 'Lunulata-4b (Combat Bow)', 'No Turning Back (Combat Bow)', 'Raconteur (Combat Bow)', 'The Spiteful Fang (Combat Bow)', 'Whispering Slab (Combat Bow)', "Whistler's Whim (Combat Bow)", "Whistler's Whim (Adept) (Combat Bow)"],
        'energy': ['Abyss Defiant (Auto Rifle)', 'Abyss Defiant (Adept) (Auto Rifle)', 'Age-Old Bond (Auto Rifle)', 'Ammit AR2 (Auto Rifle)', 'Arc Logic (Auto Rifle)', 'Arctic Haze (Auto Rifle)', 'Chrysura Melo (Auto Rifle)', 'Come to Pass (Auto Rifle)', 'Coronach-22 (Auto Rifle)', 'Dark Decider (Auto Rifle)', 'Galliard-42 (Auto Rifle)', 'Galliard-42 XN7568 (Auto Rifle)', 'Gnawing Hunger (Auto Rifle)', 'Hollow Earth (Auto Rifle)', 'Jiangshi AR4 (Auto Rifle)', 'Kibou AR3 (Auto Rifle)', "Martyr's Make (Auto Rifle)", 'Medley-45 (Auto Rifle)', 'Misfit (Auto Rifle)', 'Null Calamity 9 (Auto Rifle)', 'Perseverance (Auto Rifle)', 'Positive Outlook (Auto Rifle)', 'Prosecutor (Auto Rifle)', 'Reckless Oracle (Auto Rifle)', 'Restoration VIII (Auto Rifle)', 'Shadow Price (Auto Rifle)', 'Shadow Price (Adept) (Auto Rifle)', 'Solemn Hymn (Auto Rifle)', "Sorrow's Verse (Auto Rifle)", 'Sweet Sorrow (Auto Rifle)', 'The Number (Auto Rifle)', 'The Ringing Nail (Auto Rifle)', 'The Summoner (Auto Rifle)', 'The Summoner (Adept) (Auto Rifle)', "Uriel's Gift (Auto Rifle)", 'Valakadyn (Auto Rifle)', 'Arsenic Bite-4b (Combat Bow)', 'Hush (Combat Bow)', 'Imperial Needle (Combat Bow)', 'Point of the Stag (Combat Bow)', 'Pre Astyanax IV (Combat Bow)', 'Pre Astyanax IV (Adept) (Combat Bow)', 'Strident Whistle (Combat Bow)', 'Subtle Calamity (Combat Bow)', 'The Vow (Combat Bow)', 'Tripwire Canary (Combat Bow)', 'Tyranny of Heaven (Combat Bow)', 'Under Your Skin (Combat Bow)', 'Wolftone Draw (Combat Bow)', 'Cartesian Coordinate (Fusion Rifle)', 'Conjecture TSc (Fusion Rifle)', 'Coriolis Force (Fusion Rifle)', 'Critical Sass (Fusion Rifle)', 'Dream Breaker (Fusion Rifle)', 'Elatha FR4 (Fusion Rifle)', "Exile's Curse (Fusion Rifle)", "Exile's Curse (Adept) (Fusion Rifle)", 'Gallant Charge (Fusion Rifle)', 'Glacioclasm (Fusion Rifle)', 'Hollow Words (Fusion Rifle)', 'Iota Draconis (Fusion Rifle)', 'Iterative Loop (Fusion Rifle)', 'Likely Suspect (Fusion Rifle)', 'Loaded Question (Fusion Rifle)', 'Loaded Question (Adept) (Fusion Rifle)', 'Main Ingredient (Fusion Rifle)', "Midha's Reckoning (Fusion Rifle)", "Midha's Reckoning (Harrowed) (Fusion Rifle)", 'Nox Echo III (Fusion Rifle)', 'Nox Veneris II (Fusion Rifle)', 'Null Composure (Fusion Rifle)', 'PLUG ONE.1 (Fusion Rifle)', 'PLUG ONE.1 (Adept) (Fusion Rifle)', 'Proelium FR3 (Fusion Rifle)', 'Royal Executioner (Fusion Rifle)', 'Shock and Awe (Fusion Rifle)', 'Snorri FR5 (Fusion Rifle)', 'Techeun Force (Fusion Rifle)', 'Tempered Dynamo (Fusion Rifle)', "The Emperor's Envy (Fusion Rifle)", 'The Epicurean (Fusion Rifle)', 'The Eremite (Fusion Rifle)', 'The Wizened Rebuke (Fusion Rifle)', "Timelines' Vertex (Fusion Rifle)", 'Trinary System (Fusion Rifle)', "Zealot's Reward (Fusion Rifle)", 'Albedo Wing (Glaive)', 'Ecliptic Distaff (Glaive)', 'Greasy Luck (Glaive)', 'Judgment of Kelgorath (Glaive)', "Lubrae's Ruin (Glaive)", "Lubrae's Ruin (Adept) (Glaive)", "Nezarec's Whisper (Glaive)", 'The Enigma (Glaive)', 'Unexpected Resurgence (Glaive)', 'Unexpected Resurgence (Adept) (Glaive)'],
        'power': ['Acantha-D (Grenade Launcher)', 'Acantha-D XK8434 (Grenade Launcher)', 'Acosmic (Grenade Launcher)', "Berenger's Memory (Grenade Launcher)", 'Blast Battue (Grenade Launcher)', 'Bushwhacker (Grenade Launcher)', 'Canis Major (Grenade Launcher)', 'Cataphract GL3 (Grenade Launcher)', 'Cataphract GL3 (Adept) (Grenade Launcher)', 'Courageous Surrender (Grenade Launcher)', 'Crowd Pleaser (Grenade Launcher)', 'Cry Mutiny (Grenade Launcher)', 'Dimensional Hypotrochoid (Grenade Launcher)', 'Doomsday (Grenade Launcher)', 'Edge Transit (Grenade Launcher)', 'I Am Alive (Grenade Launcher)', 'Interference VI (Grenade Launcher)', "Koraxis's Distress (Grenade Launcher)", "Koraxis's Distress (Adept) (Grenade Launcher)", 'Love and Death (Grenade Launcher)', 'Marsilion-C (Grenade Launcher)', 'Memory Interdict (Grenade Launcher)', 'Orthrus (Grenade Launcher)', 'Outrageous Fortune (Grenade Launcher)', 'Play of the Game (Grenade Launcher)', 'Regnant (Grenade Launcher)', 'Sunrise GL4 (Grenade Launcher)', 'Swarm of the Raven (Grenade Launcher)', 'Tarnation (Grenade Launcher)', 'Terran Wind (Grenade Launcher)', "The Day's Fury (Grenade Launcher)", 'The Permanent Truth (Grenade Launcher)', 'Through Fire and Flood (Grenade Launcher)', 'Typhon GL5 (Grenade Launcher)', 'Wendigo GL3 (Grenade Launcher)', 'Wendigo GL3 (Adept) (Grenade Launcher)', 'Wicked Sister (Grenade Launcher)', "Briar's Contempt (Linear Fusion Rifle)", "Briar's Contempt (Adept) (Linear Fusion Rifle)", 'Cataclysmic (Linear Fusion Rifle)', 'Cataclysmic (Adept) (Linear Fusion Rifle)', "Corsair's Wrath (Linear Fusion Rifle)", 'Crooked Fang-4fr (Linear Fusion Rifle)', 'Dead-Ender (Linear Fusion Rifle)', 'Fire and Forget (Linear Fusion Rifle)', 'Komodo-4FR (Linear Fusion Rifle)', 'Laser Painter (Linear Fusion Rifle)', 'Line in the Sand (Linear Fusion Rifle)', "Man o' War (Linear Fusion Rifle)", "Reed's Regret (Linear Fusion Rifle)", "Reed's Regret (Adept) (Linear Fusion Rifle)", 'Sailspy Pitchglass (Linear Fusion Rifle)', 'Stormchaser (Linear Fusion Rifle)', 'Taipan-4fr (Linear Fusion Rifle)', 'Tarantula (Linear Fusion Rifle)', 'Threaded Needle (Linear Fusion Rifle)', '21% Delirium (Machine Gun)', 'A Fine Memorial (Machine Gun)', "Archon's Thunder (Machine Gun)", 'Avalanche (Machine Gun)', 'Bane of Sorrow (Machine Gun)', 'Chain of Command (Machine Gun)', 'Circular Logic (Machine Gun)','Commemoration (Machine Gun)','Corrective Measure (Machine Gun)','Corrective Measure (Timelost) (Machine Gun)', 'Edgewise (Machine Gun)', 'Eleatic Principle (Machine Gun)', 'Fixed Odds (Machine Gun)', 'Hammerhead (Machine Gun)', "Planck's Stride (Machine Gun)", 'Qua Xaphan V (Machine Gun)', "Qullim's Terminus (Machine Gun)", "Qullim's Terminus (Harrowed) (Machine Gun)", 'Recurrent Impact (Machine Gun)', 'Retrofit Escapade (Machine Gun)', 'Seventh Seraph SAW (Machine Gun)', 'Shattered Cipher (Machine Gun)', 'Song of Ir Yût (Machine Gun)', 'Song of Ir Yût (Adept) (Machine Gun)', 'Temporal Clause (Machine Gun)', 'Terminus Horizon (Machine Gun)', 'THE SWARM (Machine Gun)', 'THE SWARM (Adept) (Machine Gun)', 'Thermal Erosion (Machine Gun)', 'Unwavering Duty (Machine Gun)', 'Unwavering Duty (Adept) (Machine Gun)', 'Apex Predator (Rocket Launcher)', 'Ascendancy (Rocket Launcher)', 'Bad Omens (Rocket Launcher)', 'Bellowing Giant (Rocket Launcher)', 'Blowout (Rocket Launcher)', 'Blue Shift (Rocket Launcher)', 'BrayTech Osprey (Rocket Launcher)', 'BrayTech Osprey (Adept) (Rocket Launcher)', 'Broadsword Launcher (Rocket Launcher)', 'Bump in the Night (Rocket Launcher)', 'Classical-42 (Rocket Launcher)', 'Code Duello (Rocket Launcher)', 'Cold Comfort (Rocket Launcher)', 'Countess SA-2 (Rocket Launcher)', 'Crowning Duologue (Rocket Launcher)', 'Curtain Call (Rocket Launcher)', 'Heretic (Rocket Launcher)', 'Hezen Vengeance (Rocket Launcher)', 'Hezen Vengeance (Timelost) (Rocket Launcher)', 'Hoosegow (Rocket Launcher)', 'Hoosegow XE5837 (Rocket Launcher)', 'Morrigan-D (Rocket Launcher)', 'Mos Epoch III (Rocket Launcher)', 'Palmyra-B (Rocket Launcher)', 'Pentatonic-48 (Rocket Launcher)', 'Pit Launcher (Rocket Launcher)', 'Pyroclastic Flow (Rocket Launcher)', 'Red Herring (Rocket Launcher)', 'Roar of the Bear (Rocket Launcher)', 'Royal Entry (Rocket Launcher)', 'Scipio-D (Rocket Launcher)', 'Semiotician (Rocket Launcher)', 'Shining Sphere (Rocket Launcher)', 'Sins of the Past (Rocket Launcher)', 'Sleepless (Rocket Launcher)', 'Subzero Salvo (Rocket Launcher)', 'The Button (Rocket Launcher)', 'The Hothead (Rocket Launcher)', 'The Hothead (Adept) (Rocket Launcher)', 'Tiebreaker (Rocket Launcher)', "Tomorrow's Answer (Rocket Launcher)", "Tomorrow's Answer (Adept) (Rocket Launcher)", 'Zenobia-D (Rocket Launcher)', 'Abide the Return (Sword)', 'Bequest (Sword)', 'Caretaker (Sword)', 'Complex Solution (Sword)', 'Double-Edged Answer (Sword)', 'Falling Guillotine (Sword)', 'Future Safe 10 (Sword)', 'Geodetic HSm (Sword)', 'Hagakure (Sword)', 'Half-Truths (Sword)', 'Hero of Ages (Sword)', "Honor's Edge (Sword)", 'It Stared Back (Sword)', 'Just in Case (Sword)', 'Nasreddin (Sword)', 'Negative Space (Sword)', 'Night Terror (Sword)', "Razor's Edge (Sword)", "Sola's Scar (Sword)", "Sola's Scar (Adept) (Sword)", 'Steel Sybil Z-14 (Sword)', "Stryker's Sure-Hand (Sword)", "Temptation's Hook (Sword)", 'The Other Half (Sword)', 'Thin Precipice (Sword)', "Traitor's Fate (Sword)", 'Unspoken Promise (Sword)', 'Zephyr (Sword)']
    },
    'perks.armor': {
        'head': {
            '1': {'Discipline mod': 3,
                'Minor Discipline mod': 1,
                'Stranght mod': 3,
                'Minor Stranght mod': 1,
                'Intellect mod': 4,
                'Minor Intellect mod': 2,
                'Mobility mod': 3,
                'Minor Mobility mod': 1,
                'Recovery mod': 4,
                'Minor Recovery mod': 2,
                'Resilience mod': 4,
                'Minor Resilience mod': 2},
            '2': {'Special Ammo Finder': 3,
                'Special Ammo Scout': 1,
                'Heavy Ammo Finder': 3,
                'Heavy Ammo Scout': 1,
                'Dynamo': 3,
                'Ashes to Assets': 3,
                'Hands-on': 3,
                'Power Preservation': 3,
                'Radiant light': 1,
                'Powerful Friends': 1,
                'Font of Wisdom': 3,
                'Harmonic Siphon': 1,
                'Kinetic Siphon': 2,
                'Ark Siphon': 3,
                'Solar Siphon': 3,
                'Stasis Siphon': 3,
                'Strand Siphon': 3,
                'Void Siphon': 3,
                'Harmonic Targeting': 2,
                'Kinetic Targeting': 3,
                'Ark Targeting': 3,
                'Solar Targeting': 3,
                'Stasis Targeting': 3,
                'Strand Targeting': 3,
                'Void Targeting': 3}
        },
        'arms': {
            '1': {'Discipline mod': 3,
                'Minor Discipline mod': 1,
                'Stranght mod': 3,
                'Minor Stranght mod': 1,
                'Intellect mod': 4,
                'Minor Intellect mod': 2,
                'Mobility mod': 3,
                'Minor Mobility mod': 1,
                'Recovery mod': 4,
                'Minor Recovery mod': 2,
                'Resilience mod': 4,
                'Minor Resilience mod': 2},
			'2': {'Fastball': 1,
                'Firepower': 3,
                'Momentum Transfer': 2,
                'Bolstering Detonation': 2,
                'Grenade Kickstart': 3,
                'Font of Focus': 3,
                'Heavy Handed': 3,
                'Impact Induction': 2,
                'Focusing Strike': 2,
                'Melee Kickstart': 3,
                'Font of Vigor': 3,
                'Shield Break Charge': 4,
                'Harmonic Loader': 2,
                'Kinetic Loader': 3,
                'Ark Loader': 3,
                'Solar Loader': 3,
                'Stasis Loader': 3,
                'Strand Loader': 3,
                'Void Loader': 3,
                'Harmonic Dexterity': 2,
                'Kinetic Dexterity': 3,
                'Ark Dexterity': 3,
                'Solar Dexterity': 3,
                'Stasis Dexterity': 3,
                'Strand Dexterity': 3,
                'Void Dexterity': 3}
        },
        'torso': {
			'1': {'Discipline mod': 3,
                'Minor Discipline mod': 1,
                'Stranght mod': 3,
                'Minor Stranght mod': 1,
                'Intellect mod': 4,
                'Minor Intellect mod': 2,
                'Mobility mod': 3,
                'Minor Mobility mod': 1,
                'Recovery mod': 4,
                'Minor Recovery mod': 2,
                'Resilience mod': 4,
                'Minor Resilience mod': 2},
            '2': {'Harmonic Resistance': 1,
                'Ark Resistance': 2,
                'Solar Resistance': 2,
                'Stasis Resistance': 2,
                'Void Resistance': 2,
                'Concussive Dampener': 3,
                'Melee Damage Resistance': 3,
                'Sniper Damage Resistance': 3,
                'Emergency Reinforcement': 3,
                'Font of Endurance': 3,
                'Charged Up': 3,
                'Lucent Blades': 2,
                'Unflinching Harmonic Aim': 2,
                'Unflinching Kinetic Aim': 3,
                'Unflinching Ark Aim': 3,
                'Unflinching Solar Aim': 3,
                'Unflinching Stasis Aim': 3,
                'Unflinching Strand Aim': 3,
                'Unflinching Void Aim': 3,
                'Harmonic Reserves': 2,
                'Kinetic Reserves': 3,
                'Ark Reserves': 3,
                'Solar Reserves': 3,
                'Stasis Reserves': 3,
                'Strand Reserves': 3,
                'Void Reserves': 3}
        },
		'legs': {
			'1': {'Discipline mod': 3,
                'Minor Discipline mod': 1,
                'Stranght mod': 3,
                'Minor Stranght mod': 1,
                'Intellect mod': 4,
                'Minor Intellect mod': 2,
                'Mobility mod': 3,
                'Minor Mobility mod': 1,
                'Recovery mod': 4,
                'Minor Recovery mod': 2,
                'Resilience mod': 4,
                'Minor Resilience mod': 2},
			'2': {'Recuperation': 1,
                'Better Already': 1,
                'Innervation': 1,
                'Invigoration': 1,
                'Insulation': 1,
                'Absolution': 3,
                'Orbs of Restoration': 2,
                'Stacks on Stacks': 4,
                'Elemental Chrge': 3,
                'Kinetic Weapon Surge': 3,
                'Ark Weapon Surge': 3,
                'Solar Weapon Surge': 3,
                'Stasis Weapon Surge': 3,
                'Strand Weapon Surge': 3,
                'Void Weapon Surge': 3,
                'Font of Agility': 3,
                'Harmonic Holster': 1,
                'Kinetic Holster': 2,
                'Ark Holster': 2,
                'Solar Holster': 2,
                'Stasis Holster': 2,
                'Strand Holster': 2,
                'Void Holster': 2,
                'Harmonic Scavenger': 1,
                'Kinetic Scavenger': 1,
                'Ark Scavenger': 1,
                'Solar Scavenger': 1,
                'Stasis Scavenger': 1,
                'Strand Scavenger': 1,
                'Void Scavenger': 1}
		},
		'bandage': {
			'1': {'Discipline mod': 3,
                'Minor Discipline mod': 1,
                'Stranght mod': 3,
                'Minor Stranght mod': 1,
                'Intellect mod': 4,
                'Minor Intellect mod': 2,
                'Mobility mod': 3,
                'Minor Mobility mod': 1,
                'Recovery mod': 4,
                'Minor Recovery mod': 2,
                'Resilience mod': 4,
                'Minor Resilience mod': 2},
			'2': {'Distribution': 3,
                'Outreach': 1,
                'Bomber': 1,
                'Utility Kickstart': 3,
                'Font of Restoration': 3,
                'Time Dilation': 3,
                'Powerful Attraction': 2,
                'Proximity Ward': 2,
                'Restorative Finisher' :1,
                'Special Finisher': 1,
                'One-two Finisher': 1,
                'Bulwark Finisher': 1,
                'Healthy Finisher': 1,
                'Snapload Finisher': 1,
                'Explosive Finisher': 1,
                'Utility Finisher': 1,
                'Benevolent Finisher': 1,
                'Empowered Finish': 1,
                'Reaper': 3}
        },
    }
}


'''Sends a message after accepting the command, offers a choice of registration or login.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('sign in')
    btn2 = types.KeyboardButton('register')
    markup.row(btn1, btn2)
    file = open(os.path.join("Photo_game", "Hello.jpg"), 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, 'Приветствую вас, я бот-помощник,\n и с моей помощью вы сможете создавать и публиковать сборки для игры Destiny 2. \nНайдя подходящуую вы можете с легкостью ее просмотреть, а также оценивать. В настоящее время доступны все функции кроме удаления, она работает неисправно. ', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


'''At the user's choice, it goes to the login ot registration.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def on_click(message):
    global users
    conn = sqlite3.connect('users.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name vachar(50),pass varchar(50), rating_count INTEGER, count_voice INTEGER, all_class TEXT, all_element TEXT)')
    conn.commit()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    if message.text == 'sign in':
        bot.send_message(message.chat.id, 'Введите свой nickname', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, signiner)
    elif message.text == 'register':
        bot.send_message(message.chat.id, 'Введите свой будещий nickname', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, registering)
    else:
        bot.send_message(message.chat.id, 'Введите верную команду')
        bot.register_next_step_handler(message, on_click)


'''The login function, accepts a login, asks for a password, or offers registration.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def signiner(message):
    global users
    global nickname
    o = 0
    for user in users:
        if message.text.strip() == user[1]:
            o = 1
            nickname = message.text.strip()
            bot.send_message(message.chat.id, 'Введите пароль')
            bot.register_next_step_handler(message, passworder)
    if o == 0:
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('sign in')
        btn2 = types.KeyboardButton('register')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Такого пользователя нет, введите верный nickname, либо зарегистрируйтесь', reply_markup=markup)
        bot.register_next_step_handler(message, signiner_other)


'''Harm prevents incorrect input from the previous functin.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def signiner_other(message):
    if message.text == 'sign in':
        bot.send_message(message.chat.id, 'Введите свой nickname повторно', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, signiner)
    elif message.text == 'register':
        bot.send_message(message.chat.id, 'Введите свой будещий nickname', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, registering)
    else:
        bot.send_message(message.chat.id, 'Введите верную команду')
        bot.register_next_step_handler(message, signiner_other)


'''Entering a password, verifying its validity.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def passworder(message):
    global users
    global nickname
    global password
    o = 0
    for user in users:
        if message.text.strip() == user[2] and nickname == user[1]:
            o = 1
            password == user[2]
            bot.send_message(message.chat.id, 'Вы вошли,поздравляю', reply_markup=main_buttons())
            bot.register_next_step_handler(message, main)
    if o == 0:
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('enter password')
        btn2 = types.KeyboardButton('register')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Пароль не подходит, введите верный, либо зарегистрируйтесь', reply_markup=markup)
        bot.register_next_step_handler(message, passworder_other)


'''Harm prevents incorrect input from the previous functin.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def passworder_other(message):
    if message.text == 'enter password':
        bot.send_message(message.chat.id, 'Введите свой пароль повторно', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, passworder)
    elif message.text == 'register':
        bot.send_message(message.chat.id, 'Введите свой будещий nickname', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, registering)
    else:
        bot.send_message(message.chat.id, 'Введите верную команду')
        bot.register_next_step_handler(message, passworder_other)


'''Registering function. Accepts a name and asks for a password.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def registering(message):
    global nickname
    global users
    o = 0
    for el in users:
        if message.text.strip() == el[1]:
            o = 1
    if o == 0:
        nickname = message.text.strip()
        bot.send_message(message.chat.id, 'введи пароль')
        bot.register_next_step_handler(message, pas_registering)
    else:
        bot.send_message(message.chat.id, 'Такой пользователь уже существует, выберите другой nickname')
        bot.register_next_step_handler(message, registering)


'''Re-enterig the password.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def pas_registering(message):
    global password
    password = message.text.strip()
    bot.send_message(message.chat.id, 'введи пароль повторно')
    bot.register_next_step_handler(message, fin_registering)


'''Cheking for password matches, in the positive case, the user is logged into the database.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def fin_registering(message):
    global nickname
    global password
    if password == message.text.strip():
        conn = sqlite3.connect('users.sql')
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, pass, rating_count, count_voice,all_class, all_element) VALUES("%s","%s","%s","%s","%s","%s")' % (nickname, password, 0, 0, '0', '0'))
        conn.commit()
        cur.close()
        conn.close()
        bot.send_message(message.chat.id, 'вы зареганы', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    else:
        bot.send_message(message.chat.id, 'Ваши пароли не совпадают,введите заново')
        bot.register_next_step_handler(message, pas_registering)


'''The main body of the program, choice: create an build, all builds, user builds, log out and delete account.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def main(message):
    global users
    global password
    global nickname
    global buildes
    global all_info_game
    global build
    global na_au
    global markup_speshal
    na_au = nickname
    conn = sqlite3.connect('users.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    conn = sqlite3.connect('buildes.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS buildes(id INTEGER PRIMARY KEY, name TEXT, name_build TEXT, rating INTEGER, raiting_count INTEGER, value TEXT)')
    cur.execute('SELECT * FROM buildes')
    buildes = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    conn = sqlite3.connect('mark.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS mark(id INTEGER PRIMARY KEY, name TEXT, name_build TEXT, name_voice TEXT, mark INTEGER)')
    conn.commit()
    cur.close()
    conn.close()
    if message.text == 'Выход из системы':
        password = ''
        nickname = ''
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, 'Вы вышли из системы', reply_markup=markup)
        bot.register_next_step_handler(message, start)
    elif message.text == 'Мои сборки':
        bot.send_message(message.chat.id, f'Вывожу все сборки от пользователя {nickname}', reply_markup=buildes_from_player_buttons('--all_build--', nickname))
        bot.register_next_step_handler(message, buildes_from_player)
    elif message.text == 'Сборки сообщества':
        bot.send_message(message.chat.id, 'Выводятся сборки подождите немного...', reply_markup=list_buildes_buttons('--all--'))
        bot.send_message(message.chat.id, 'Вы можете пользоваться кнопками, либо испольбзовать клавиатуру для частичного поиска по имени автора, классу, стихии, доступные у автора.')
        bot.register_next_step_handler(message, list_buildes)
    elif message.text == 'Создать сборку':
        build = ['']*3
        markup = types.ReplyKeyboardMarkup()
        for class_ in all_info_game['classes']:
            markup.add(types.KeyboardButton(class_))
        markup_speshal = markup
        bot.send_message(message.chat.id, 'Выберите класс персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, choose_class)
    elif message.text == 'Удалить акаунт':
        bot.send_message(message.chat.id, 'Вы точно в этом уверены, удаление акаунта происходит безвозвратно, будут утеряны все сборки, а также ваш рейтинг. Вы полноценно воспринимаете все риски и соглашаетесь, что при удалении вы потеряете все данные, связанные с этим акаунтом?', reply_markup=double_button())
        bot.register_next_step_handler(message, your_choose)
    else:
        bot.send_message(message.chat.id, 'Введите верную команду')
        bot.register_next_step_handler(message, main)


'''Buttons for the block main.

:return Markup
 '''
def main_buttons():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Мои сборки')
    btn2 = types.KeyboardButton('Сборки сообщества')
    markup.row(btn1, btn2)
    markup.add(types.KeyboardButton('Создать сборку'))
    btn1 = types.KeyboardButton('Выход из системы')
    btn2 = types.KeyboardButton('Удалить акаунт')
    markup.row(btn1, btn2)
    return markup


'''Starting to create a build, selecting a class.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_class(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    if message.text.strip() in all_info_game['classes']:
        time_out = 0
        conclusion(message, message.text.strip())
        while time_out == 0:
            a = 1
        if time_out == 1:
            markup = types.ReplyKeyboardMarkup()
            for elem in all_info_game['element']:
                markup.add(types.KeyboardButton(elem))
            markup_speshal = markup
            build[0] = message.text.strip()
            bot.send_message(message.chat.id, 'Выберите стихию персонажа', reply_markup=markup)
            bot.register_next_step_handler(message, choose_element)
        else:
            bot.register_next_step_handler(message, choose_class)
    else:
        bot.send_message(message.chat.id, 'Выберите верный класс персонажа')
        bot.register_next_step_handler(message, choose_class)


'''Continuing to create a build, choosing an element.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_element(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    if message.text.strip() in all_info_game['element']:
        time_out = 0
        conclusion(message, message.text.strip())
        while time_out == 0:
            a = 1
        if time_out == 1:
            build[1] = message.text.strip()
            markup = types.ReplyKeyboardMarkup()
            for sup_abil in all_info_game['super.ability'][build[0]][build[1]]:
                markup.add(types.KeyboardButton(sup_abil))
            markup_speshal = markup
            bot.send_message(message.chat.id, 'Выберите супер способность персонажа', reply_markup=markup)
            bot.register_next_step_handler(message, choose_super_ability)
        else:
            bot.register_next_step_handler(message, choose_element)

    else:
        bot.send_message(message.chat.id, 'Выберите верную стихию персонажа')
        bot.register_next_step_handler(message, choose_element)


'''Continuing to create a build, choosing a super ability.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_super_ability(message):
    global build
    global all_info_game
    global time_out
    if message.text.strip() in all_info_game['super.ability'][build[0]][build[1]]:
        time_out = 0
        conclusion(message, message.text.strip())
        while time_out == 0:
            a = 1
        if time_out == 1:
            build[2] = message.text.strip()
            choose_ability_start(message)
        else:
            bot.register_next_step_handler(message, choose_super_ability)
    else:
        bot.send_message(message.chat.id, 'Выберите верную супер способность персонажа')
        bot.register_next_step_handler(message, choose_super_ability)


'''Continuing to create a build, create a buttons for ability.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_ability_start(message):
    global build
    global all_info_game
    global markup_speshal
    global markup_index
    global name_ability
    markup_speshal = []
    name_ability = []
    for class_abil in all_info_game['ability'][build[0]][build[1]].keys():
        markup = types.ReplyKeyboardMarkup()
        for abil in all_info_game['ability'][build[0]][build[1]][class_abil]:
            markup.add(types.KeyboardButton(abil))
        markup_speshal.append(markup)
        name_ability.append(class_abil)
    markup_index = 0
    bot.send_message(message.chat.id, f'Выберите способность из {name_ability[markup_index]}', reply_markup=markup_speshal[0])
    bot.register_next_step_handler(message, choose_ability)


'''Continuing to create a build, create a buttons for artefacts.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_artefacts_start(message):
    global build
    global all_info_game
    global markup_speshal
    global markup_index
    markup_speshal = []
    for count_mod in range(2):
        time_out = 1
        markup = types.ReplyKeyboardMarkup()
        for mod in all_info_game['artefacts'][build[0]][build[1]]:
            markup.add(types.KeyboardButton(mod))
        markup_speshal.append(markup)
    markup_index = 0
    bot.send_message(message.chat.id, f'Выберите {markup_index+1}-й артефакт подкласса', reply_markup=markup)
    bot.register_next_step_handler(message, choose_artefacts)


'''Continuing to create a build, create a buttons for modification ability.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_modification_ability_start(message):
    global build
    global all_info_game
    global markup_speshal
    global markup_index
    markup_speshal = []
    for count_mod in range(4):
        markup = types.ReplyKeyboardMarkup()
        for mod in all_info_game['modification.ability'][build[0]][build[1]]:
            markup.add(types.KeyboardButton(mod))
        markup_speshal.append(markup)
    markup_index = 0
    bot.send_message(message.chat.id, f'Выберите {markup_index+1}-е улучшение подкласса', reply_markup=markup_speshal[markup_index])
    bot.register_next_step_handler(message, choose_modification_ability)


'''Continuing to create a build, create a buttons for exotic armor.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_exotic_armor_start(message):
    global build
    global all_info_game
    global markup_speshal

    armor_list = all_info_game['exotic.armor'][build[0]]
    markup = types.ReplyKeyboardMarkup()
    for armor in range(0, len(armor_list), 2):
        btn1 = types.KeyboardButton(armor_list[armor])
        if armor + 1 < len(armor_list):
            btn2 = types.KeyboardButton(armor_list[armor+1])
            markup.row(btn1, btn2)

        else:
            markup.add(btn1)
    markup_speshal = markup
    bot.send_message(message.chat.id, 'Выберите экзотическую броню', reply_markup=markup)
    bot.register_next_step_handler(message, choose_exotic_armor)


'''Continuing to create a build, choosing an ability.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_ability(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    global markup_index
    global name_ability
    o = 0
    for el in all_info_game['ability'][build[0]][build[1]].values():
        if message.text.strip() in el:
            time_out = 0
            conclusion(message, message.text.strip())
            while time_out == 0:
                a = 1
            o = 1
            if time_out == 1:
                o = 2
                build.append(message.text.strip())
                break
            else:
                bot.register_next_step_handler(message, choose_ability)
    if o == 0:
        bot.send_message(message.chat.id, 'Выберите верную способность персонажа')
        bot.register_next_step_handler(message, choose_ability)
    elif o == 2:
        markup_index += 1
        if markup_index == len(name_ability):
            choose_artefacts_start(message)
        else:
            bot.send_message(message.chat.id, f'Выберите способность из {name_ability[markup_index]}', reply_markup=markup_speshal[markup_index])
            bot.register_next_step_handler(message, choose_ability)


'''Continuing to create a build, choosing an artefacts.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_artefacts(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    global markup_index
    el = all_info_game['artefacts'][build[0]][build[1]]
    if message.text.strip() in el and build[-1] != message.text.strip():
        time_out = 0
        conclusion(message, message.text.strip())
        while time_out == 0:
            a = 1
        if time_out == 1:
            build.append(message.text.strip())
            time_out_wait = 1
            markup_index += 1
            if markup_index == len(markup_speshal):
                choose_modification_ability_start(message)
            else:
                bot.send_message(message.chat.id, f'Выберите {markup_index+1}-й артефакт подкласса', reply_markup=markup_speshal[markup_index])
                bot.register_next_step_handler(message, choose_artefacts)
        else:
            bot.register_next_step_handler(message, choose_artefacts)

    else:
        bot.send_message(message.chat.id, 'Выберите верный артефакт персонажа')
        bot.register_next_step_handler(message, choose_artefacts)


'''Continuing to create a build, choosing an modification ability.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_modification_ability(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    global markup_index
    el = all_info_game['modification.ability'][build[0]][build[1]]
    if message.text.strip() in el:
        if not (message.text.strip() in build[-4:]):
            time_out = 0
            conclusion(message, message.text.strip())
            while time_out == 0:
                a = 1
            if time_out == 1:
                build.append(message.text.strip())
                markup_index += 1
                if markup_index == len(markup_speshal):
                    choose_exotic_armor_start(message)
                else:
                    bot.send_message(message.chat.id, f'Выберите {markup_index+1}-е улучшение подкласса', reply_markup=markup_speshal[markup_index])
                    bot.register_next_step_handler(message, choose_modification_ability)
            else:
                bot.register_next_step_handler(message, choose_modification_ability)
        else:
            bot.send_message(message.chat.id, 'Выберите верное улучшение подкласса, эта уже использованна')
            bot.register_next_step_handler(message, choose_modification_ability)
    else:
        bot.send_message(message.chat.id, 'Выберите верное улучшение подкласса')
        bot.register_next_step_handler(message, choose_modification_ability)


'''Continuing to create a build, choosing an exotic armor.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_exotic_armor(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal

    if message.text.strip() in all_info_game['exotic.armor'][build[0]]:
        time_out = 0
        conclusion(message, message.text.strip())
        while time_out == 0:
            a = 1
        if time_out == 1:
            build.append(message.text.strip())

            markup = types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton('none'))
            for weap in all_info_game['exotic.weapons'].keys():
                markup.add(types.KeyboardButton(weap))

            bot.send_message(message.chat.id, 'Выберите экзотическое оружие', reply_markup=markup)
            bot.register_next_step_handler(message, choose_class_exotic_weapons)
        else:
            bot.register_next_step_handler(message, choose_exotic_armor)

    else:
        bot.send_message(message.chat.id, 'Выберите верную экзот броню')
        bot.register_next_step_handler(message, choose_exotic_armor)


'''Continuing to create a build, choosing the type of exotic weapons.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_class_exotic_weapons(message):
    global build
    global all_info_game
    global markup_speshal
    global markup_index
    global legendary_class
    legendary_class = []
    markup_speshal = []
    if message.text.strip() == 'none':
        for class_weap in all_info_game['legendary.weapons'].keys():
            time_out = 1
            markup = types.ReplyKeyboardMarkup()
            weap_list = all_info_game['legendary.weapons'][class_weap]

            for weap in range(0, len(weap_list), 2):
                btn1 = types.KeyboardButton(weap_list[weap])
                if weap + 1 < len(weap_list):
                    btn2 = types.KeyboardButton(weap_list[weap+1])
                    markup.row(btn1, btn2)
                else:
                    markup.add(btn1)
            legendary_class.append(class_weap)
            markup_speshal.append(markup)

        markup_index = 0
        bot.send_message(message.chat.id, f'Выберите легендарное {legendary_class[markup_index]} оружие', reply_markup=markup_speshal[markup_index])
        bot.register_next_step_handler(message, choose_legendary_weapons)

    elif message.text.strip() in all_info_game['exotic.weapons'].keys():
        markup = types.ReplyKeyboardMarkup()
        class_weap_ex = message.text.strip()
        ex_weap_list = all_info_game['exotic.weapons'][message.text.strip()]
        for ex_weap in range(0, len(ex_weap_list), 2):
            btn1 = types.KeyboardButton(ex_weap_list[ex_weap])
            if ex_weap + 1 < len(ex_weap_list):
                btn2 = types.KeyboardButton(ex_weap_list[ex_weap+1])
                markup.row(btn1, btn2)
            else:
                markup.add(btn1)

        markup_speshal.append(markup)
        legendary_class.append(0)

        for class_weap in all_info_game['legendary.weapons'].keys():
            if class_weap != class_weap_ex:
                markup = types.ReplyKeyboardMarkup()
                weap_list = all_info_game['legendary.weapons'][class_weap]
                for weap in range(0, len(weap_list), 2):
                    btn1 = types.KeyboardButton(weap_list[weap])
                    if weap + 1 < len(weap_list):
                        btn2 = types.KeyboardButton(weap_list[weap+1])
                        markup.row(btn1, btn2)
                    else:
                        markup.add(btn1)
                legendary_class.append(class_weap)
                markup_speshal.append(markup)

        markup_index = 0
        bot.send_message(message.chat.id, f'Выберите экзот {class_weap_ex} оружие', reply_markup=markup_speshal[markup_index])
        bot.register_next_step_handler(message, choose_exotic_weapons)
    else:
        bot.send_message(message.chat.id, 'Выберите существующее оружие', reply_markup=markup)
        bot.register_next_step_handler(message, choose_class_exotic_weapons)


'''Continuing to create a build, create a buttons for items armor.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_items_armor(message):
    global build
    global all_info_game
    global markup_speshal
    global markup_index
    global items_class

    markup_speshal = []
    items_class = []
    for items in all_info_game['perks.armor'].keys():
        items_class.append(items)
        perk_list = list(all_info_game['perks.armor'][items]['1'].keys())
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('none'))
        for perk in range(0, len(perk_list), 2):
            btn1 = types.KeyboardButton(perk_list[perk])
            if perk + 1 < len(perk_list):
                btn2 = types.KeyboardButton(perk_list[perk+1])
                markup.row(btn1, btn2)
            else:
                markup.add(btn1)
        markup_speshal.append(markup)
        for count in range(3):
            markup = types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton('none'))
            perk_list = list(all_info_game['perks.armor'][items]['2'].keys())
            for perk in range(0, len(perk_list), 2):
                btn1 = types.KeyboardButton(perk_list[perk])
                if perk + 1 < len(perk_list):
                    btn2 = types.KeyboardButton(perk_list[perk+1])
                    markup.row(btn1, btn2)
                else:
                    markup.add(btn1)
            markup_speshal.append(markup)
    markup_index = 0
    bot.send_message(message.chat.id, f'Выберите первый перк для {items_class[markup_index//4]}', reply_markup=markup_speshal[markup_index])
    bot.register_next_step_handler(message, choose_perks_armor)


'''Continuing to create a build, choosing the exotic weapons.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_exotic_weapons(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    global markup_index
    global legendary_class
    o = 0
    for el in all_info_game['exotic.weapons']:
        if message.text.strip() in all_info_game['exotic.weapons'][el]:
            time_out = 0
            o = 1
            conclusion(message, message.text.strip())
            while time_out == 0:
                a = 1
            if time_out == 1:
                build.append(message.text.strip())
                markup_index += 1
                bot.send_message(message.chat.id, f'Выберите легендарное {legendary_class[markup_index]} оружие', reply_markup=markup_speshal[markup_index])
                bot.register_next_step_handler(message, choose_legendary_weapons)
            else:
                bot.register_next_step_handler(message, choose_exotic_weapons)

            break
    if o == 0:
        bot.send_message(message.chat.id, 'Введите верное екзот оружие')
        bot.register_next_step_handler(message, choose_exotic_weapons)


'''Continuing to create a build, choosing the legendary weapons to the remaining slots.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_legendary_weapons(message):
    global build
    global all_info_game
    global time_out
    global markup_speshal
    global markup_index
    global legendary_class
    o = 0
    for el in all_info_game['legendary.weapons']:
        if message.text.strip() in all_info_game['legendary.weapons'][el]:
            time_out = 0
            o = 1
            conclusion(message, message.text.strip())
            while time_out == 0:
                a = 1
            if time_out == 1:
                build.append(message.text.strip())
                markup_index += 1
                if markup_index == len(markup_speshal):
                    choose_items_armor(message)
                else:
                    bot.send_message(message.chat.id, f'Выберите легендарное {legendary_class[markup_index]} оружие', reply_markup=markup_speshal[markup_index])
                    bot.register_next_step_handler(message, choose_legendary_weapons)
            else:
                bot.register_next_step_handler(message, choose_legendary_weapons)
    if o == 0:
        bot.send_message(message.chat.id, 'Введите верное легендарное оружие')
        bot.register_next_step_handler(message, choose_legendary_weapons)


'''Continuing to create a build, choosing the perks armor.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def choose_perks_armor(message):
    global build
    global all_info_game
    global energy
    global time_out
    global energy
    global markup_speshal
    global markup_index
    global items_class
    o = 0
    if markup_index % 4 == 0:
        energy = 0
    time_out = 0
    list_perk = ['первый', 'второй', 'третий', 'четвертый']
    if message.text.strip() == 'none':
        bot.send_message(message.chat.id, f'egergy {energy}/10')
        markup_index += 1
        build.append(message.text.strip())
        if markup_index == len(markup_speshal):
            bot.send_message(message.chat.id, 'А теперь придумай описание,чтоб все знали как использовать сборку, не используя символ <#>', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, description)
        else:
            bot.send_message(message.chat.id, f'Выберите {list_perk[markup_index%4]} перк для {items_class[markup_index//4]}', reply_markup=markup_speshal[markup_index])
            bot.register_next_step_handler(message, choose_perks_armor)
    elif message.text.strip() in all_info_game['perks.armor'][items_class[markup_index//4]]['2'].keys():
        k = '2'
        o = 1
    elif message.text.strip() in all_info_game['perks.armor'][items_class[markup_index//4]]['1'].keys():
        k = '1'
        o = 1
    else:
        bot.send_message(message.chat.id, 'Введите верный перк')
        bot.register_next_step_handler(message, choose_perks_armor)
    if o == 1:
        conclusion(message, message.text.strip())
        while time_out == 0:
            a = 1
        if time_out == 1:
            if energy + all_info_game['perks.armor'][items_class[markup_index//4]][k][message.text.strip()] <= 10:
                energy += all_info_game['perks.armor'][items_class[markup_index//4]][k][message.text.strip()]
                build.append(message.text.strip())
                bot.send_message(message.chat.id, f'egergy {energy}/10')
                markup_index += 1
                if markup_index == len(markup_speshal):
                    bot.send_message(message.chat.id, 'А теперь придумай описание,чтоб все знали как использовать сборку, не используя символ <#>', reply_markup=types.ReplyKeyboardRemove())
                    bot.register_next_step_handler(message, description)
                else:
                    bot.send_message(message.chat.id, f'Выберите {list_perk[markup_index%4]} перк для {items_class[markup_index//4]}', reply_markup=markup_speshal[markup_index])
                    bot.register_next_step_handler(message, choose_perks_armor)
            else:
                bot.send_message(message.chat.id, 'Ваша энергия переполнена,выберите заново', reply_markup=markup_speshal[markup_index])
                bot.register_next_step_handler(message, choose_perks_armor)
        else:
            bot.register_next_step_handler(message, choose_perks_armor)


'''Continuing to create a build, choosing the info of build without '#' to conect later.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def description(message):
    global build
    if not ('#' in message.text):
        build.append(message.text)
        bot.send_message(message.chat.id, 'А теперь назови свою сборку', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, build_name)
    else:
        bot.send_message(message.chat.id, 'Создай описание без символа <#>', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, description)


'''Continuing to create a build, choosing the name of build.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def build_name(message):
    global build
    global all_info_game
    global nickname
    conn = sqlite3.connect('buildes.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM buildes')
    s = cur.fetchall()
    m = 0
    for el in s:
        if el[2] == message.text.strip():
            m = 1
    if m == 0:
        value = '#'.join(map(str, build))

        conn = sqlite3.connect('buildes.sql')
        cur = conn.cursor()
        cur.execute("INSERT INTO buildes (name, name_build, rating, raiting_count, value) VALUES (?,?,?,?,?)", (nickname, message.text.strip(), 0, 0, value))
        conn.commit()
        cur.close()
        conn.close()
        conn = sqlite3.connect('users.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        s = cur.fetchall()
        for el in s:
            if el[1] == nickname:
                if el[5] == '0':
                    cur.execute("UPDATE users SET all_class = ?, all_element = ? WHERE name = ?", (build[0], build[1], nickname))
                    conn.commit()
                    cur.close()
                    conn.close()
                    break
                else:
                    classes = super_sorted(el[5], build[0])
                    elem = super_sorted(el[6], build[1])
                    cur.execute("UPDATE users SET all_class = ?, all_element = ? WHERE name = ?", (classes, elem, nickname))
                    conn.commit()
                    cur.close()
                    conn.close()
                    break
        view_build(message, nickname, message.text.strip())
    else:
        bot.send_message(message.chat.id, 'Такое название уже используется, введите другое')
        bot.register_next_step_handler(message, build_name)


'''Continuing to create a build, choosing the name of build.

:params str1: some string
:type str1: str
:params str1: some string
:type str1: str
:return Correctly combined string
 '''
def super_sorted(str1, str2):
    return ','.join(sorted(list(set(str1.split(',') + str2.split()))))


'''The function outputs the build by key parameters.

:params message: the object that transmits the user's message
:type message: telebot
:params title_use: username
:type title_use: str
:params title_build_user: build name
:type title_build_user: str
:return None
 '''
def view_build(message, title_user, title_build_user):
    global time_out_wait
    global nickname
    global na_au
    global title_build_user1
    title_build_user1 = title_build_user
    conn = sqlite3.connect('buildes.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM buildes')
    a = cur.fetchall()
    for el in a:
        if title_build_user in el[2] and title_user in el[1]:
            if el[4] == 0:
                rait = el[3]
            else:
                rait = el[3]/el[4]
            pre_view = el[5].split('#')
            break
    info = pre_view[-1]
    pre_view = pre_view[:-1]
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f'СБОРКА {title_build_user} ОТ {title_user} С РЕЙТИНГОМ {rait}/5.0')
    bot.send_message(message.chat.id, f'Info: {info}')
    for el in [[0, 1], [1, 3], [3, 5], [5, 7], [7, 9], [9, -24], [-24, -22], [-22, -20], [-20, -16], [-16, -12], [-12, -8], [-8, -4], [-4, -1]]:
        time_out_wait = 0
        send_group_photo(message, el[0], el[1], pre_view)
        while time_out_wait != 1:
            a = 1
    if na_au != nickname:
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('Оценить'))
        markup.add(types.KeyboardButton('Воздержаться'))
        bot.send_message(message.chat.id, 'Оцените сборку', reply_markup=markup)
        bot.register_next_step_handler(message, mark_question)
    else:
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('Оставить сборку на сохранении'))
        markup.add(types.KeyboardButton('Удалить сборку, мне не нравится'))
        bot.send_message(message.chat.id, 'Все готово!', reply_markup=markup)
        bot.register_next_step_handler(message, dell_build_quetion)


'''The function outputs photos in group.

:params message: the object that transmits the user's message
:type message: telebot
:params from_: the left border of the output
:type from_: int
:params to_: the rigth border of the output
:type to_: int
:params pre_view: the build itself
:type pre_view: list
:return None
 '''
def send_group_photo(message, from_, to_, pre_view):
    global time_out_wait
    file = []
    if to_ == -1:
        a = pre_view[from_:]
    else:
        a = pre_view[from_:to_]
    for el in a:
        name = f'{el}.jpg'
        file.append(telebot.types.InputMediaPhoto(open(os.path.join("Photo_game", name), 'rb')))
    bot.send_media_group(message.chat.id, file)
    time_out_wait = 1


'''An offer to the user to evaluate someone else's build.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def mark_question(message):
    if message.text.strip() == 'Оценить':
        markup = types.ReplyKeyboardMarkup()
        markes = []
        for mark in range(6):
            markes.append(types.KeyboardButton(str(mark)))
        markup.row(markes[0], markes[1], markes[2])
        markup.row(markes[3], markes[4], markes[5])
        bot.send_message(message.chat.id, 'Оцените сборку', reply_markup=markup)
        bot.register_next_step_handler(message, mark_)
    elif message. text.strip() == 'Воздержаться':
        bot.send_message(message.chat.id, 'Вас понял.', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, пользуйтесь кнопками.')
        bot.register_next_step_handler(message, mark_question)


'''Choosing a score from 0 to 5 for the first time.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def mark_(message):
    global nickname
    global mark_us
    global mark_us_new
    global na_au
    global title_build_user1
    if message.text.strip() in ['0', '1', '2', '3', '4', '5']:
        conn = sqlite3.connect('mark.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM mark')
        markes = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        a = 0
        for mark in markes:
            if nickname == mark[3] and na_au == mark[1] and title_build_user1 == mark[2]:
                a = 1
                mark_us = mark[4]
        mark_us_new = int(message.text.strip())
        if a == 1:
            bot.send_message(message.chat.id, f'Вы собираетесь поменять оценку с {mark_us} на {mark_us_new}?', reply_markup=double_button())
            bot.register_next_step_handler(message, mark_change)
        else:
            bot.send_message(message.chat.id, f'Вы собираетесь поставить оценку {mark_us_new} этой сборке?', reply_markup=double_button())
            bot.register_next_step_handler(message, mark_choose)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, пользуйтесь кнопками.')
        bot.register_next_step_handler(message, mark_)


'''Choosing a score from 0 to 5 repeatedly.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def mark_change(message):
    global nickname
    global na_au
    global mark_us
    global mark_us_new
    global title_build_user1
    if message.text.strip() == 'Yes':
        conn = sqlite3.connect('mark.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM mark')
        cur.execute("UPDATE mark SET mark = ? WHERE name = ? and name_build = ? and name_voice = ?", (mark_us_new, na_au, title_build_user1, nickname))
        conn.commit()
        cur.close()
        conn.close()
        conn = sqlite3.connect('users.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        a = cur.fetchall()
        for el in a:
            if el[1] == na_au:
                rating_count = el[3]
        cur.execute("UPDATE users SET rating_count = ? WHERE name = ?", (rating_count - mark_us + mark_us_new, na_au))
        conn.commit()
        cur.close()
        conn.close()

        conn = sqlite3.connect('buildes.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM buildes')
        a = cur.fetchall()
        for el in a:
            if el[1] == na_au and el[2] == title_build_user1:
                rating_count = el[3]
        cur.execute("UPDATE buildes SET rating = ? WHERE name = ? and name_build = ?", (rating_count - mark_us + mark_us_new, na_au, title_build_user1))
        conn.commit()
        cur.close()
        conn.close()
        bot.send_message(message.chat.id, f'Ваша оценка именена с {mark_us} на {mark_us_new}', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    elif message.text.strip() == 'No':
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('Оценить'))
        markup.add(types.KeyboardButton('Воздержаться'))
        bot.send_message(message.chat.id, 'Попробуйте снова', reply_markup=markup)
        bot.register_next_step_handler(message, mark_question)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, пользуйтесь кнопками.')
        bot.register_next_step_handler(message, mark_change)


'''Confirmation of the mark selection.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def mark_choose(message):
    global nickname
    global na_au
    global mark_us_new
    global title_build_user1
    if message.text.strip() == 'Yes':
        conn = sqlite3.connect('mark.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM mark')
        cur.execute("INSERT INTO mark (name,name_build,name_voice,mark) VALUES (?,?,?,?)", (na_au, title_build_user1, nickname, mark_us_new))
        conn.commit()
        cur.close()
        conn.close()

        conn = sqlite3.connect('users.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        a = cur.fetchall()
        for el in a:
            if el[1] == na_au:
                rating_count = el[3]
                count_voice = el[4]
        cur.execute("UPDATE users SET rating_count = ?, count_voice = ? WHERE name = ?", (rating_count + mark_us_new, count_voice + 1, na_au))
        conn.commit()
        cur.close()
        conn.close()

        conn = sqlite3.connect('buildes.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM buildes')
        a = cur.fetchall()
        for el in a:
            if el[1] == na_au and el[2] == title_build_user1:
                rating = el[3]
                raiting_count = el[4]
        cur.execute("UPDATE buildes SET rating = ?, raiting_count = ? WHERE name = ? and name_build = ?", (rating + mark_us_new, raiting_count + 1, na_au, title_build_user1))
        conn.commit()
        cur.close()
        conn.close()
        bot.send_message(message.chat.id, f'Ваша оценка {mark_us_new} записана', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    elif message.text.strip() == 'No':
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('Оценить'))
        markup.add(types.KeyboardButton('Воздержаться'))
        bot.send_message(message.chat.id, 'Попробуйте снова', reply_markup=markup)
        bot.register_next_step_handler(message, mark_question)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, пользуйтесь кнопками.')
        bot.register_next_step_handler(message, mark_choose)


'''Deleting an assembly and all records about it.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def dell_build_quetion(message):
    global title_build_user1
    global time_out_replace
    if message.text.strip() == 'Удалить сборку, мне не нравится':
        time_out_replace = 0
        bot.send_message(message.chat.id, 'Операция производится, подождите...')
        dell_build(title_build_user1)
        while time_out_replace != 1:
            a = 1
        bot.send_message(message.chat.id, 'Все готово! Сборка удалена', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    elif message.text.strip() == 'Оставить сборку на сохранении':
        bot.send_message(message.chat.id, 'Все готово!', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, пользуйтесь кнопками.')
        bot.register_next_step_handler(message, dell_build_quetion)


'''The function of delete build.

:params title_build: name of build which  will be daleted
:type title_build: str
:return None
 '''
def dell_build(title_build):
    global nickname
    global time_out_replace
    conn1 = sqlite3.connect('users.sql')
    cur1 = conn1.cursor()
    cur1.execute('SELECT * FROM users')
    a = cur1.fetchall()
    for el in a:
        if el[1] == nickname:
            score1 = el[3]
            count1 = el[4]
    conn = sqlite3.connect('buildes.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM buildes')
    a = cur.fetchall()
    for el in a:
        if el[1] == nickname and el[2] == title_build:
            score = el[3]
            count = el[4]
    cur1.execute("UPDATE users SET rating_count = ?, count_voice = ? WHERE name = ?", (score1 - score, count1 - count, nickname))
    conn1.commit()

    cur.execute("DELETE FROM buildes WHERE name = ? and name_build = ?", (nickname, title_build))
    conn.commit()
    cur.close()
    conn.close()
    cur1.close()
    conn1.close()

    conn = sqlite3.connect('mark.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM mark WHERE name_voice = ? and name_build = ?", (nickname, title_build))
    conn.commit()
    cur.close()
    conn.close()
    time_out_replace = 1


'''The function outputs two buttons yes and no.

:return Markup
 '''
def double_button():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Yes')
    btn2 = types.KeyboardButton('No')
    markup.row(btn1, btn2)
    return markup


'''The function displays the photo and asks whether the user has chosen.

:params message: the object that transmits the user's message
:type message: telebot
:params message: name of the component
:type message: str
:return None
 '''
def conclusion(message, title):
    global long
    global time_out
    long = 3
    file = open(os.path.join("Photo_game", f'{title}.jpg'), 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, 'Это то,что ты хотел?', reply_markup=double_button())
    bot.register_next_step_handler(message, questioner)


'''The questioner claifies the user's choice.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def questioner(message):
    global markup_speshal
    global time_out
    global long
    global markup_index
    if type(markup_speshal) == list:
        markup_speshal_alfa = markup_speshal[markup_index]
    else:
        markup_speshal_alfa = markup_speshal

    if message.text.strip() == 'Yes':
        dell_3_message(message, long)
        time_out = 1
    elif message.text.strip() == 'No':
        time_out = 2
        dell_3_message(message, long)
        bot.send_message(message.chat.id, 'Ок, выберите заново', reply_markup=markup_speshal_alfa)
    else:
        long += 2
        bot.send_message(message.chat.id, 'Я вас не понял, повторите снова')
        bot.register_next_step_handler(message, questioner)


'''Deletes the last three messages in the chat.

:params message: the object that transmits the user's message
:type message: telebot
:params long: the number of messages that will be deleted
:type long: int
:return None
 '''
def dell_3_message(message, long):
    for el in range(long):
        bot.delete_message(message.chat.id, message.message_id - el)


'''Prepares user buttons with keywork blocks.

:params search: the name of users whose buildes will be shown
:type search: str
:return Markup
 '''
def list_buildes_buttons(search):
    conn = sqlite3.connect('users.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    a = cur.fetchall()
    all_b = []
    for el in a:
        if (search == '--all--' or search in super_join(el)) and el[5] != '0':
            k = f'Рейтинг {correct_rait(el)}'
            all_b.append(super_join(el))
    all_b = sorted(all_b)
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('--all--'))
    for el in range(0, len(all_b), 2):

        btn1 = types.KeyboardButton(all_b[el])
        if el + 1 < len(all_b):
            btn2 = types.KeyboardButton(all_b[el + 1])
            markup.row(btn1, btn2)
        else:
            markup.add(btn1)
    markup.add(types.KeyboardButton('main'))
    return markup


'''Outputs all builds from the sellected user

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def list_buildes(message):
    if message.text == '--all--':
        bot.send_message(message.chat.id, 'Вывожу всех пользователей', reply_markup=list_buildes_buttons('--all--'))
        bot.register_next_step_handler(message, list_buildes)
    elif message.text == 'main':
        bot.send_message(message.chat.id, 'Перевожу в main', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    else:
        all_b = []
        conn = sqlite3.connect('users.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        a = cur.fetchall()
        s = 0
        for el in a:
            k = f'Рейтинг {correct_rait(el)}'
            if message.text == super_join(el):
                s = 1
                bot.send_message(message.chat.id, f'Вывожу все сборки от пользователя {message.text.split(" - ")[0]}', reply_markup=buildes_from_player_buttons('--all_build--', (message.text.split(" - "))[0]))
                bot.register_next_step_handler(message, buildes_from_player)
                break
        if s == 0:
            bot.send_message(message.chat.id, f'Вывожу пользователей, где было найдено {message.text}', reply_markup=list_buildes_buttons(message.text))
            bot.register_next_step_handler(message, list_buildes)


'''Combines an array into a string.

:params mass: the array that nneds to be combined
:type mass: list
:return None
 '''
def super_join(mass):
    return " - ".join([mass[1], mass[5], mass[6]])


'''Searches for author's buildes by key.

:params search: builds search key
:type search: str
:params name_author: name of the author of the builds
:type name_author: str
:return None
 '''
def buildes_from_player_buttons(search, name_author):
    global na_au
    na_au = name_author
    conn = sqlite3.connect('buildes.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM buildes')
    a = cur.fetchall()
    all_b = []
    for el in a:
        k = f'Рейтинг {correct_rait(el)}'
        if name_author == el[1] and (search == '--all_build--' or search in " - ".join([el[2], k, (el[5].split('#'))[0], (el[5].split('#'))[1]])):
            all_b.append(" - ".join([el[2], k, (el[5].split('#'))[0], (el[5].split('#'))[1]]))
    all_b = sorted(all_b)
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('--all_build--'))
    for el in range(0, len(all_b), 2):

        btn1 = types.KeyboardButton(all_b[el])
        if el + 1 < len(all_b):
            btn2 = types.KeyboardButton(all_b[el+1])
            markup.row(btn1, btn2)
        else:
            markup.add(btn1)
    markup.add(types.KeyboardButton('main'))
    return markup


'''Outputs the selected build fromthe user.

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def buildes_from_player(message):
    global na_au
    if message.text == '--all_build--':
        bot.send_message(message.chat.id, f'Вывожу все сборки от пользователя {na_au}', reply_markup=buildes_from_player_buttons('--all_build--', na_au))
        bot.register_next_step_handler(message, buildes_from_player)
    elif message.text == 'main':
        bot.send_message(message.chat.id, 'Перевожу в main', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    else:
        all_b = []
        conn = sqlite3.connect('buildes.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM buildes')
        a = cur.fetchall()
        s = 0
        for el in a:
            k = f'Рейтинг {correct_rait(el)}'
            if message.text == " - ".join([el[2], k, (el[5].split('#'))[0], (el[5].split('#'))[1]]):
                s = 1
                bot.send_message(message.chat.id, f'Вывожу сборку {el[2]}', reply_markup=types.ReplyKeyboardRemove())
                view_build(message, el[1], el[2])
                break
        if s == 0:
            bot.send_message(message.chat.id, f'Вывожу сборки, где было найдено {message.text} от пользователя {na_au}', reply_markup=buildes_from_player_buttons(message.text, na_au))
            bot.register_next_step_handler(message, buildes_from_player)


'''Rounds it up as needed.

:params build: correct rounding
:type build: list
:return None
 '''
def correct_rait(build):
    if build[4] == 0:
        k = round(0, 2)
    else:
        k = round(build[3] / build[4], 2)
    return k


'''deletes the build

:params message: the object that transmits the user's message
:type message: telebot
:return None
 '''
def your_choose(message):
    global time_out
    if message.text == 'Yes':
        time_out = 0
        bot.send_message(message.chat.id, 'Это ваш выбор')
        dell_akk()
        while time_out != 1:
            a = 1
        password = ''
        nickname = ''
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, 'Дело сделано', reply_markup=markup)
        bot.register_next_step_handler(message, start)
    elif message.text == 'No':
        bot.send_message(message.chat.id, 'Принимаю ваш выбор', reply_markup=main_buttons())
        bot.register_next_step_handler(message, main)
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, повторите снова')
        bot.register_next_step_handler(message, your_choose)


'''Deletes everything related to the user.

:return None
 '''
def dell_akk():
    global time_out
    conn = sqlite3.connect('users.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = ?", (nickname,))
    cur.close()
    conn.close()

    conn = sqlite3.connect('buildes.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM buildes WHERE name = ?", (nickname,))
    cur.close()
    conn.close()

    conn = sqlite3.connect('mark.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM mark WHERE name_voice = ?", (nickname,))
    cur.close()
    conn.close()

    time_out = 1


bot.infinity_polling()
