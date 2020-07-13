
class MinionPool(object):

    def __init__(self):
        '''
            A startig minion pool has the following quanities of units
                Tier 1 - 16 of each unit
                Tier 2 - 15 of each unit
                Tier 3 - 13 of each unit
                Tier 4 - 11 of each unit
                Tier 5 - 9 of each unit
                Tier 6 - 7 of each unit
        '''
        self.QUANTITIES_PER_TIER = [16,15,13,11,9,7]

        self.UNITS_PER_TIER = {
            'Beasts': [
                [
                    '1Alleycat','1Scavenging Hyena'
                ],
                [
                    '2Kindly Grandmother','2Rabid Saurolisk','2Rat Pack'
                ],
                [
                    '3Houndmaster','3Infested Wolf','3Monstrous Macaw','3Pack Leader','3The Beast'
                ],
                [
                    '4Cave Hydra','4Savannah Highmane','4Virmen Sensei'
                ],
                [
                    '5Goldrinn, the Great Wolf','5Ironhide Direhorn'
                ],
                [
                    '6Ghastcoiler','6Maexxna','6Mama Bear'
                ],

            ],
            'Murlocs': [
                [
                    '1Murloc Tidecaller','1Murloc Tidecaller','1Rockpool Hunter'
                ],
                [
                    '2Murloc Warleader','2Old Murk-Eye'
                ],
                [
                    '3Coldlight Seer'
                ],
                [
                    '3Felfin Navigator'
                ],
                [
                    '4Toxfin'
                ],
                [
                    '5King Bagurgle','5Primalfin Lookout'
                ],
                [
                    '6Gentle Megasaur'
                ],
            ],
            'Pirates': [
                [
                    '1Deck Swabbie','1Scallywag'
                ],
                [
                    '2Freedealing Gambler','2Southsea Captain'
                ],
                [
                    '3Bloodsail Cannoneer','3Salty Looter','3Yo-Ho-Ogre'
                ],
                [
                    '4Goldgrubber','4Ripsnarl Captain','4Southsea Strongarm'
                ],
                [
                    "5Cap'n Hoggarr",'5Nat Pagle, Extreme Angler','5Seabreaker Goliath'
                ],
                [
                    '6Dread Admiral Eliza','6The Tide Razor'
                ],
            ],
            'Mechs': [
                [
                    '1Mecharoo','1Micro Machine'
                ],
                [
                    '2Harvest Golem','2Kaboom Bot','2Metaltooth Leaper','2Pogo-Hopper'
                ],
                [
                    '3Deflect-o-bot','3Piloted Shredder','3Replicating Menace','3Screwjank Clunker'
                ],
                [
                    '4Annoy-o-Module','4Iron Sensei','4Mechano-Egg','4Security Rover'
                ],
                [
                    '5Junkbot',"5Sneed's Old Shredder"
                ],
                [
                    '6Foe Reaper 4000',"6Kangor's Apprentice"
                ],
            ],
            'Dragon': [
                [
                    '1Dragonspawn Lieutenant','1Red Whelp'
                ],
                [
                    '2Glyph Guardian','2Steward of Time','2Waxrider Togwaggle'
                ],
                [
                    '3Bronze Warden','3Hangry Dragon','3Twilight Emissary',
                ],
                [
                    '4Cobalt Scalebane','4Drakonid Enforcer','4Herald of Flame'
                ],
                [
                    '5Murozond','5Razorgore, the Untamed'
                ],
                [
                    '6Kalecgos, Arcane Aspect','6Nadina the Red'
                ],
            ],
            'Demon': [
                [
                    '1Fiendish Servant','1Vulgar Homunculus','1Wrath Weaver'
                ],
                [
                    '2Imprisoner','2Nathrezim Overseer',
                ],
                [
                    '3Crystalweaver','3Imp Gang Boss','3Soul Juggler',
                ],
                [
                    '4Floating Watcher','4Siegebreaker',
                ],
                [
                    '5Annihilan Battlemaster',"5Mal'Ganis",'5Voidlord'
                ],
                [
                    '6Imp Mama',
                ],
            ],
            'Neutral':[
                [
                    '1Righteous Protector', '1Selfless Hero'
                ],
                [
                    '2Arcane Cannon', "2Spawn of N'Zoth",'2Unstable Ghoul','2Zoobot'
                ],
                [
                    '3Crowd Favorite', '3Khadgar','3Shifter Zerus','3Bolvar, Fireblood','3Defender of Argus',
                ],
                [
                    '4Menagerie Magician',
                ],
                [
                    '5Baron Rivendare','5Brann Bronzebeard','5Lightfang Enforcer','5Strongshell Scavenger',
                ],
                [
                    '6Zapp Slywick'
                ]
            ],
        }
