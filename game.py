from random import choice, shuffle, randint
from time import sleep

def game_24_check_operation(oper):
    allowed = '1234567890+-*/() '
    is_number = False
    for i in oper:
        if i not in allowed:
            return False
        try:
            num = int(i)
            if is_number:
                return False  # catch concatenation of numbers
            is_number = True
        except Exception:
            is_number = False
            pass
    return True

def game_24():
    all_choices = [1,2,3,4,5,6,7,8,9]
    choices = []
    for i in range(4):
        ch = choice(all_choices)
        all_choices.remove(ch)
        choices.append(ch)
    if set(choices) in [{1,6,7,8}, {3,4,6,7}]:  # unsolvable cases
        choices = [1,2,3,4]

    print(r'''
 ____  _  _  ____  
|___  \| || | / ___| __ _ _ __ ___  ___ 
 __) | || |_ | |  _ / _` | '_ ` _ \ / _ \
/ __/|__  _| | |_| | (_| | | | | | |  __/
|_____| |_|  \____|\__,_|_| |_| |_|\___|
''')
    print('Do math operations to get the number 24!')
    while True:
        print(f'Your choices are: {choices}')
        operations = input('Enter your numbers along with operations (+, -, *, /) (brackets are allowed): ')
        included_number_count = 0
        for i in choices:
            if str(i) in operations:
                included_number_count += 1
        if included_number_count != 4:
            print('Please use all 4 numbers!')
            continue
        if not game_24_check_operation(operations):
            print('Please only use allowed operations!')
            continue
        result = 0
        try:
            result = eval(operations)
        except Exception:
            print('Don\'t type gibberish!')
            continue
        result = int(result)
        if result == 24:
            print(f'You won! {operations} = {result}')
            return True
        else:
            print(f'You lose! {operations} = {result}, better luck next time!')
            return False

def game_words(diff):
    match diff:
        case 0:
            words = ["able", "aged", "agog", "aide", "airy", "ajar", "akin", "ammo",
                     "apex", "arch", "arty", "ashy", "atom", "auto", "avid", "away", "awed",
                     "baby", "band", "bank", "bark", "barn", "base", "bass", "bath",
                     "bead", "beam", "bean", "bear", "beef", "bend", "best", "bevy", "bike", "bill",
                     "bine", "blog", "blot", "blue", "blur", "boar", "bold", "bolt", "book",
                     "boot", "born", "boss", "both", "bowl", "boxy", "brag", "brim", "buff", "bulb",
                     "bump", "bunk", "burr", "busy", "cafe", "cake", "calf", "calm", "cane", "cape",
                     "card", "care", "carp", "cart", "case", "cash", "cask", "cave", "cell", "cent",
                     "chic", "chin", "chip", "chop", "city", "clad", "claw", "clay", "clef", "clip",
                     "clod", "clog", "club", "clue", "coal", "coat", "coda", "code", "coin", "colt",
                     "comb", "cook", "cool", "copy", "cord", "core", "cork", "corn", "cosy", "crab",
                     "crew", "crib", "crop", "crow", "cube", "cult", "curd", "curl", "dame", "damp",
                     "dark", "dart", "dash", "dawn", "dear", "deep", "deer", "deft", "desk", "dhal",
                     "dhow", "dial", "dice", "diet", "disc", "dish", "doer", "doll", "dome", "done",
                     "door", "dove", "dray", "drop", "drum", "dual", "duck", "duct", "dusk", "each",
                     "east", "easy", "echo", "ecru", "edge", "edgy", "envy", "epic", "euro",
                     "even", "ewer", "exam", "exit", "fain", "fair", "fall", "fare", "farm",
                     "fast", "faun", "fawn", "feet", "fell", "fern", "fife", "file", "film", "fine", "fire",
                     "firm", "fish", "five", "flag", "flat", "flax", "flea", "flex", "flit", "flue", "flux",
                     "foal", "foam", "fond", "font", "food", "fore", "form", "foxy", "free", "fuse",
                     "fuss", "gaff", "gala", "gale", "game", "gamy", "gaol", "gate", "germ",
                     "ghat", "gill", "gilt", "glad", "glue", "goal", "goat", "gold", "gone",
                     "good", "gram", "grey", "grid", "grub", "gulf", "gull", "gust", "hair", "hale",
                     "half", "hall", "hare", "hazy", "heap", "heat", "herd", "hero", "hewn",
                     "hill", "hind", "hive", "home", "hood", "hoof", "hoop", "hour", "huge",
                     "hunt", "iced", "idea", "inch", "inky", "iron", "item", "jail", "joke", "just",
                     "kame", "keel", "keen", "keep", "kelp", "kerb", "king", "kite", "knee", "knot",
                     "kohl", "lace", "lacy", "lamb", "lamp", "lane", "late", "lava", "lawn", "laze",
                     "lead", "leaf", "lean", "left", "lens", "life", "like", "limb", "line", "link", "lino",
                     "lion", "live", "load", "loaf", "loan", "loch", "loft", "logo", "lone", "long",
                     "look", "loop", "lord", "lost", "loud", "luck", "lure", "lush", "mail", "mall",
                     "mane", "many", "mast", "maze", "meal", "meet", "mega", "menu", "mere",
                     "mews", "mice", "mike", "mild", "mill", "mime", "mind", "mine",
                     "mini", "mint", "mire", "mitt", "mole", "mood", "moon", "moor",
                     "more", "moss", "most", "much", "musk", "myth", "name", "nave", "navy",
                     "neap", "near", "neat", "neck", "need", "nest", "news", "next", "nice", "nosh",
                     "note", "noun", "nova", "nowt", "null", "numb", "oast", "odds", "ogee", "once",
                     "only", "open", "oval", "over", "pace", "page", "pail", "pair",
                     "pall", "palm", "park", "part", "past", "path", "pawl", "peak",
                     "pear", "peel", "pile", "pill", "pink", "pins", "pith", "pity", "plan", "plot",
                     "plum", "plus", "poem", "poet", "pony", "pool", "pore", "port", "posh",
                     "pout", "pram", "prey", "prim", "prow", "puce", "pure", "purr", "quay", "quin",
                     "quip", "quiz", "raft", "rail", "rain", "rake", "ramp", "rare", "reed", "rent", "rest",
                     "rich", "rife", "ripe", "rise", "road", "roan", "roof", "rope", "rose", "rosy",
                     "ruby", "ruff", "rule", "rung", "rust", "safe", "saga", "sage", "sail", "sake",
                     "sale", "salt", "same", "sand", "sane", "save", "scar", "seal", "seam",
                     "seer", "sett", "shed", "ship", "shoe", "shop", "shot", "show", "side", "sign",
                     "silk", "sine", "sink", "site", "size", "skew", "skip", "slab", "sloe", "slow",
                     "slub", "snap", "snow", "snub", "snug", "sock", "sofa", "soil", "sole",
                     "solo", "some", "song", "soup", "spam", "span", "spar", "spot", "spry", "stag",
                     "star", "stem", "such", "suet", "sure", "swan", "swap", "tale", "tall", "tame",
                     "tank", "tape", "task", "taut", "taxi", "team", "tear", "teat", "tent", "term", "test",
                     "text", "then", "thud", "tick", "tide", "tidy", "tile", "till", "time", "tiny", "toad",
                     "tofu", "toga", "toil", "tomb", "tour", "town", "trad", "tram", "trap", "tray",
                     "trio", "true", "trug", "tsar", "tube", "tuna", "tune", "turf", "turn", "tusk", "twee",
                     "twig", "twin", "type", "tyre", "unit", "used", "vase", "vast", "veal",
                     "veil", "very", "vest", "view", "vote", "wail", "wall", "wand", "ward", "warm",
                     "wary", "wasp", "wave", "wavy", "waxy", "week", "weir", "well",
                     "west", "whey", "whim", "whip", "wide", "wild", "wile", "will", "wily",
                     "wind", "wing", "wipe", "wire", "wise", "wish", "wont", "wool",
                     "worn", "wove", "wren", "yawl", "yawn", "year", "yoke", "yolk", "zany", "zing"]
        case 1:
            words = ["ackee", "actor", "acute", "adept", "afoot", "agile", "aglow",
                     "alarm", "album", "alert", "alike", "alive", "alkyl", "alloy", "alone",
                     "alpha", "amber", "ample", "angle", "apple", "apron", "arena",
                     "argon", "arrow", "aside", "astir", "atlas", "attic", "audio", "aunty", "avail",
                     "awake", "award", "aware", "awash", "axial", "azure", "badge", "baggy",
                     "balmy", "barge", "basal", "basic", "basin", "basis", "baths", "baton", "baulk",
                     "beach", "beads", "beady", "beefy", "beery", "beige", "bench", "berry", "bhaji",
                     "bidet", "bijou", "bitty", "blank", "blase", "blaze", "bling", "bliss",
                     "block", "bloke", "blond", "blues", "blurb", "board", "bonny", "bonus", "booth",
                     "boric", "bound", "bower", "brake", "brass", "brave", "break", "bream",
                     "bride", "brief", "briny", "brisk", "broad", "broom", "brown", "bugle",
                     "built", "bulky", "bumpy", "bunch", "cabin", "cable", "cairn", "calyx", "canny",
                     "canoe", "canto", "caret", "cargo", "chain", "chalk", "charm", "chart", "chary",
                     "chess", "chest", "chewy", "chief", "chill", "chine", "chive", "choir",
                     "chump", "cinch", "civic", "civil", "claim", "clank", "class", "clear", "clerk",
                     "cliff", "cloak", "clock", "close", "cloth", "cloud", "clove", "clump", "coach",
                     "coast", "cocoa", "combe", "comfy", "comic", "comma", "conic",
                     "coomb", "copse", "coral", "corps", "court", "coven", "cover", "crane",
                     "crate", "crisp", "croak", "crony", "crowd", "crown", "crumb", "crust",
                     "cubic", "curly", "curve", "daily", "dairy", "daisy", "dance", "dazed",
                     "delta", "demob", "denim", "diary", "digit", "diner", "dinky", "disco", "ditch",
                     "diver", "divot", "dizzy", "dodge", "domed", "doubt", "dozen", "draft", "drain",
                     "drama", "drawl", "drawn", "dream", "dress", "dried", "drier", "drill", "drink",
                     "drive", "droll", "drone", "duple", "dusky", "dusty", "eager", "eagle", "early",
                     "eater", "elder", "elect", "elfin", "elite", "email", "envoy", "epoch", "equal",
                     "error", "ether", "ethic", "event", "every", "exact", "extra", "facet", "faint",
                     "famed", "fancy", "farad", "fated", "feast", "fence", "ferny", "ferry", "fever",
                     "fibre", "fiery", "filmy", "final", "finch", "fishy", "fizzy", "flash",
                     "flask", "fleet", "flick", "flies", "flock", "flood", "floor", "flour", "fluid",
                     "flush", "flute", "focal", "focus", "foggy", "force", "forge", "forty",
                     "fount", "frame", "frank", "fresh", "front", "frost", "frown", "funny", "furry",
                     "furze", "futon", "fuzzy", "gable", "gamma", "gamut", "gauzy", "gecko",
                     "ghost", "giant", "giddy", "given", "glace", "glass", "glaze", "gleam",
                     "globe", "glory", "glove", "gluey", "going", "goods", "goody", "gooey",
                     "goose", "gorse", "gouge", "gourd", "grace", "grain", "grand", "grape",
                     "graph", "grasp", "great", "green", "groat", "group", "grown", "guard", "guest",
                     "guide", "guise", "gummy", "gusty", "hanky", "happy", "hardy", "hasty",
                     "heads", "heaps", "heavy", "hedge", "hefty", "helix", "herby", "hertz", "hewer",
                     "hilly", "hinge", "hobby", "holey", "homey", "honey", "hoppy", "hotel",
                     "humid", "husky", "hutch", "hyena", "icing", "ideal", "image",
                     "imago", "index", "inner", "ionic", "irons", "ivory", "jacks", "jaggy", "jammy",
                     "jazzy", "jeans", "jelly", "jewel", "jokey", "jolly", "juice", "jumbo",
                     "jumpy", "kazoo", "khaki", "kiosk", "knife", "knurl", "koala", "label", "laird",
                     "large", "larky", "larva", "laser", "lasso", "latex", "lathe", "latte", "layer",
                     "leafy", "leaky", "least", "ledge", "leech", "leggy", "lemon", "lento", "level",
                     "lever", "lilac", "limit", "linen", "liner", "litre", "loads", "loamy",
                     "local", "lofty", "logic", "lolly", "loose", "lorry", "loser", "lotto", "lower",
                     "lucid", "lucky", "lunar", "lunch", "lupin", "lyric", "magic",
                     "major", "malty", "mango", "marly", "marsh", "maser", "match", "matey",
                     "maths", "mauve", "mayor", "mealy", "meaty", "medal", "media", "mercy",
                     "merry", "metal", "meter", "metre", "micro", "miner", "minty", "misty",
                     "mixed", "mixer", "modal", "model", "molar", "month", "moral",
                     "motel", "motet", "mothy", "motor", "motte", "mould",
                     "mouse", "mousy", "mouth", "movie", "muddy", "mulch", "mural", "music",
                     "musty", "muted", "natty", "naval", "navvy", "newel", "newsy", "nifty", "night",
                     "ninja", "noble", "noise", "nomad", "north", "notch", "noted", "novel",
                     "oaken", "ocean", "olden", "olive", "onion", "onset", "orbit", "order",
                     "other", "outer", "overt", "owing", "oxide", "ozone", "pacer", "pager",
                     "paint", "pally", "palmy", "panda", "paper", "party", "pasty", "patch", "pause",
                     "peace", "peach", "peaky", "pearl", "peaty", "peeve", "pence", "penny",
                     "perch", "perky", "petal", "phone", "photo", "piano", "pilot", "pitch", "pithy",
                     "piton", "place", "plain", "plane", "plank", "plant", "plumy", "plush",
                     "point", "polar", "polka", "porch", "posse", "pouch", "pound", "pouty", "power",
                     "prank", "prawn", "price", "pride", "prime", "prior", "prism", "privy",
                     "prize", "prone", "proof", "prose", "proud", "pulpy", "pupal",
                     "pupil", "puppy", "puree", "purse", "quark", "quart", "query", "quest", "quick",
                     "quiet", "quill", "quilt", "quirk", "quits", "radar", "radio", "rainy",
                     "rally", "ranch", "range", "rapid", "raven", "razor", "ready", "recap", "redox",
                     "reedy", "regal", "reign", "relay", "remit", "reply", "resit", "retro", "rhyme",
                     "rider", "ridge", "rifle", "right", "rigid", "rimed", "risky", "river", "roast",
                     "robin", "robot", "rocky", "rooms", "roomy", "roost", "round", "route", "royal",
                     "ruler", "runic", "rural", "rusty", "sable", "salad", "salon", "sassy",
                     "sated", "satin", "saute", "scale", "scaly", "scant", "scarf", "scent", "scoop",
                     "scope", "scrub", "scuff", "sedge", "senna", "sense", "sepia", "seven", "shade",
                     "shaky", "shale", "shame", "shank", "shape", "shark", "sharp", "sheer", "sheet",
                     "shelf", "shell", "shiny", "shirt", "shoal", "shock", "shore", "short", "shrug",
                     "shtum", "sieve", "sight", "silky", "silty", "sixer", "skate", "skill", "skirl",
                     "slang", "slaty", "sleek", "sleet", "slice", "slide", "slime", "small", "smart",
                     "smelt", "smoke", "smoky", "snack", "snail", "snake", "snare", "sniff", "snore",
                     "snowy", "solar", "solid", "sonic", "soppy", "sorry", "sound",
                     "soupy", "south", "space", "spare", "spark", "spate", "spawn", "spear",
                     "spent", "spicy", "spiel", "spike", "spire", "spite", "splay", "spoon", "sport",
                     "spout", "spree", "squad", "stack", "staff", "stage", "staid", "stain", "stair",
                     "stamp", "stand", "stare", "start", "state", "steak", "steam", "steel",
                     "steep", "stern", "stick", "still", "stock", "stoic", "stone", "stony",
                     "stool", "store", "stork", "storm", "story", "stout", "strap", "straw", "stray",
                     "stuck", "study", "style", "suave", "sugar", "sunny", "sunup", "super", "surge",
                     "swarm", "sweet", "swell", "swift", "swipe", "swish", "sword",
                     "sworn", "syrup", "table", "tacit", "tamer", "tangy", "taper", "tarry", "taste",
                     "tawny", "tenon", "tense", "tenth", "terms", "terse", "theme", "these",
                     "thief", "third", "thorn", "those", "three", "tiara", "tidal", "tiger", "tight", "tilde",
                     "tiled", "tined", "tinny", "tipsy", "tired", "title", "toast", "today", "token",
                     "tonal", "tonic", "topic", "torch", "torte", "total", "towel", "tower",
                     "trail", "train", "treat", "trial", "tribe", "trice", "trike", "trill", "trout", "truce",
                     "truck", "trunk", "truss", "truth", "twain", "tweak", "twine", "twirl",
                     "uncut", "undue", "union", "upper", "urban", "usual", "utter", "vague", "valid",
                     "value", "vegan", "verse", "video", "visit", "vista", "vital", "vocal", "voice",
                     "vowel", "wacky", "wagon", "waist", "washy", "watch", "water", "waxen",
                     "weave", "weber", "weeny", "weird", "whale", "wheat", "whiff", "whole",
                     "whorl", "widow", "width", "wince", "winch", "windy", "wiper", "wispy",
                     "witty", "woody", "wordy", "world", "worth", "wound", "wreck", "wrist",
                     "yacht", "yogic", "young", "youth", "yummy", "zebra", "zippy", "zonal"]
        case 2:
            words = ["ablaze", "access", "acting", "action", "active", "actual",
                     "acuity", "adagio", "adroit", "adverb", "advice", "aerial", "aflame", "afloat",
                     "agency", "airway", "alight", "allied", "allure", "amazed", "amoeba", "amount",
                     "anchor", "annual", "answer", "apeman", "apical", "arable", "arbour",
                     "arcane", "ardent", "ardour", "armful", "armlet", "armour", "arrant", "artful",
                     "artist", "asleep", "aspect", "asthma", "astral", "astute", "atomic", "august",
                     "auntie", "autumn", "avatar", "badger", "ballet", "banner", "barber", "bardic",
                     "barley", "barrel", "basics", "basket", "bathos", "batten", "battle", "beaded",
                     "beaked", "beaker", "bedbug", "bedsit", "beetle", "belief", "benign", "better",
                     "billow", "binary", "bionic", "biotic", "blazon", "blithe", "blotch", "blouse",
                     "blower", "bluish", "blurry", "bonded", "bonnet", "bonsai", "border", "botany",
                     "bottle", "bounds", "bovine", "breach", "breath", "breeze", "breezy", "brewer",
                     "bridge", "bright", "bronze", "brooch", "bubbly", "bucket", "buckle",
                     "budget", "bumper", "bundle", "burger", "burrow", "button",
                     "buzzer", "bygone", "byroad", "cachet", "cactus", "camera", "campus",
                     "canape", "candid", "candle", "canine", "canned", "canopy", "canvas", "carbon",
                     "career", "carpet", "carrot", "carton", "castle", "casual", "catchy",
                     "catnap", "cattle", "causal", "caveat", "caviar", "celery", "cellar", "cement",
                     "centre", "cereal", "cerise", "chalky", "chance", "chancy", "change",
                     "chatty", "cheery", "cheese", "chilly", "chirpy", "choice", "choral",
                     "chorus", "chummy", "chunky", "cinder", "cinema", "circle", "circus", "classy",
                     "claves", "clayey", "clever", "clinic", "cloche", "cobweb", "cocoon", "coeval",
                     "coffee", "coffer", "cogent", "collar", "collie", "colour", "column", "comedy",
                     "common", "conger", "conoid", "convex", "cookie", "cooler", "coping",
                     "copper", "cordon", "corned", "corner", "cosmic", "county",
                     "coupon", "course", "covert", "cowboy", "coyote", "cradle", "craggy", "crayon",
                     "creaky", "credit", "crispy", "crumby", "crunch", "cuboid", "cupola", "curacy",
                     "cursor", "curtsy", "custom", "cyclic", "dainty", "damper", "dapper", "daring",
                     "dative", "dazzle", "debate", "debtor", "decent", "defect", "degree", "deluxe",
                     "demure", "denary", "desert", "desire", "detail", "device", "dexter", "diatom",
                     "dilute", "dimple", "dinghy", "direct", "divide", "divine", "docile", "doctor",
                     "dogged", "doodle", "dotage", "doting", "dotted", "double", "doughy", "dragon",
                     "drapes", "drawer", "dreamy", "dressy", "dulcet", "duplex", "earthy", "earwig",
                     "echoey", "effect", "effort", "eighty", "either", "elated", "eldest", "elfish",
                     "elixir", "embryo", "ending", "energy", "engine", "enough", "entire",
                     "equine", "eraser", "ermine", "errant", "ersatz", "excise", "excuse", "exempt",
                     "exotic", "expert", "expiry", "extant", "fabled", "facile", "factor",
                     "fallow", "family", "famous", "farmer", "fecund", "feisty", "feline", "fellow",
                     "fencer", "ferric", "fervid", "fierce", "figure", "filial", "fillip", "finish", "finite",
                     "fiscal", "fitful", "fitted", "flambe", "flaxen", "fleece", "fleecy", "flight",
                     "flinty", "floral", "florid", "flossy", "floury", "flower", "fluent", "fluffy",
                     "fodder", "foible", "folder", "folksy", "forage", "forest", "formal", "former",
                     "fridge", "frieze", "fright", "frilly", "frizzy", "frosty", "frothy", "frozen",
                     "frugal", "funnel", "future", "gabled", "gaffer", "gaiter", "galaxy",
                     "gallon", "galore", "gaming", "gaoler", "garage", "garden", "garlic", "gentle",
                     "gerbil", "gifted", "giggly", "ginger", "girder", "glassy", "glider", "glitzy",
                     "global", "glossy", "gloved", "golden", "gopher", "gowned", "grainy",
                     "grassy", "grater", "gratis", "gravel", "grease", "greasy", "greeny", "grilse",
                     "gritty", "groove", "grotto", "ground", "grubby", "grungy", "guitar", "gutter",
                     "hairdo", "haloed", "hamlet", "hammer", "hanger", "hawser", "header", "health",
                     "helper", "hempen", "herbal", "hermit", "heroic", "hiccup", "hinder", "hinged",
                     "homely", "homing", "honest", "hoofed", "hooked", "horsey", "hostel",
                     "hourly", "hubbub", "huddle", "humane", "humble", "humour", "hungry",
                     "hunted", "hunter", "hurray", "hybrid", "hyphen", "iambic", "icicle", "iconic",
                     "iguana", "immune", "inborn", "indoor", "inland", "inmost", "innate", "inrush",
                     "insect", "inside", "instep", "intact", "intent", "intern", "invite",
                     "inward", "iodine", "ironic", "island", "italic", "jacket", "jagged", "jailer",
                     "jargon", "jaunty", "jingle", "jingly", "jockey", "jocose", "jocund", "jogger",
                     "joggle", "jovial", "joyful", "joyous", "jumble", "jumper", "jungly", "junior",
                     "kennel", "ketone", "kettle", "kilted", "kindly", "kingly", "kirsch", "kitbag",
                     "kitten", "knight", "ladder", "landed", "laptop", "larder", "larval", "latest",
                     "latter", "laurel", "lavish", "lawful", "lawyer", "layman", "leaded", "leaden",
                     "league", "ledger", "legacy", "legend", "legion", "lemony", "lender", "length",
                     "lepton", "lessee", "lesser", "lesson", "lethal", "letter", "liable", "lidded",
                     "likely", "limber", "limpid", "lineal", "linear", "liquid", "lissom", "listed",
                     "litter", "little", "lively", "livery", "living", "lizard", "loaded", "loafer",
                     "locker", "locust", "logger", "lordly", "lounge", "lovely", "loving", "lugger",
                     "lupine", "lustre", "luxury", "madcap", "magnet", "maiden",
                     "malted", "mammal", "manful", "manned", "manner", "mantis", "manual",
                     "marble", "margin", "marine", "marked", "market", "maroon", "marshy",
                     "mascot", "massif", "matrix", "matted", "matter", "mature", "meadow",
                     "medial", "median", "medium", "memory", "merest", "meteor", "method",
                     "metric", "mickle", "midday", "middle", "mighty", "milieu",
                     "minded", "minute", "mirror", "missus", "moated", "mobile",
                     "modern", "modest", "modish", "module", "mohair", "molten", "moment",
                     "mosaic", "motion", "motive", "motley", "moving", "muckle",
                     "mucous", "muddle", "mulish", "mulled", "mullet", "museum", "mutiny",
                     "mutton", "mutual", "muzzle", "myopia", "myriad", "mystic",
                     "mythic", "nachos", "narrow", "nation", "native", "natter", "nature", "nearby",
                     "nether", "nettle", "neuter", "newish", "nimble", "nobody", "normal", "notice",
                     "nought", "number", "object", "oblate", "oblong", "occult", "octane",
                     "ocular", "oddity", "offcut", "office", "oldish", "oniony", "online", "onrush",
                     "onside", "onward", "opaque", "opener", "orange", "origin", "ornate",
                     "orphan", "osprey", "outfit", "owlish", "oxtail", "oxygen", "packed", "packet",
                     "palace", "paltry", "papery", "parade", "parcel", "parody", "parrot", "patchy",
                     "patent", "pathos", "pavane", "peachy", "peaked", "peanut", "pebble", "pebbly",
                     "pedlar", "people", "pepper", "petite", "petrol", "phrase", "picker", "picket",
                     "pickle", "picnic", "pigeon", "pillar", "pillow", "pimple", "pimply", "pincer",
                     "pinion", "piping", "pitted", "placid", "planar", "planet", "plaque", "plenty",
                     "pliant", "plucky", "plumed", "plummy", "plunge", "plural", "plushy",
                     "pocked", "pocket", "poetic", "poetry", "poised", "polite", "pollen",
                     "porous", "postal", "poster", "potato", "potted", "pounce", "powder", "precis",
                     "prefix", "pretty", "pricey", "primal", "profit", "prompt", "proper", "proven",
                     "public", "puddle", "pulley", "pulsar", "punchy", "puppet", "purism", "purist",
                     "purple", "purply", "puzzle", "quaint", "quango", "quasar", "quirky", "rabbit",
                     "racing", "racket", "radial", "radius", "raffia", "raffle", "ragged", "raging",
                     "raglan", "ragtag", "raisin", "rammer", "ramrod", "random", "rapper",
                     "raring", "rarity", "rasher", "rating", "ration", "rattle", "ravine", "raving",
                     "reason", "rebate", "recent", "recess", "recipe", "record", "redial",
                     "reform", "regent", "region", "relief", "relish", "remark", "remiss", "remote",
                     "rennet", "rennin", "repair", "report", "rested", "result", "retort", "revamp",
                     "reward", "rhythm", "ribbon", "ridden", "riddle", "ridged", "ripple", "rising",
                     "robust", "rocket", "rodent", "rotary", "rotund", "roving", "rubble", "ruched",
                     "rudder", "rueful", "rugged", "rugger", "rumour", "rumpus", "runway", "russet",
                     "rustic", "rustle", "rutted", "saddle", "saithe", "saline", "salmon", "sample",
                     "sandal", "sateen", "satiny", "saucer", "saving", "sawfly", "scalar",
                     "scales", "scarab", "scarce", "scenic", "scheme", "school", "schtum", "scorer",
                     "scrawl", "screen", "script", "scurfy", "season", "seated", "second", "secret",
                     "secure", "sedate", "seemly", "select", "senior", "sensor", "septet",
                     "serene", "serial", "series", "settee", "setter", "severe", "shaper", "sharer",
                     "sheeny", "shield", "shiner", "shorts", "shovel", "shower", "shrewd", "shrill",
                     "shrimp", "signal", "signet", "silage", "silent", "silken", "silver",
                     "simian", "simile", "simper", "simple", "sinewy", "single", "sinter",
                     "sister", "sketch", "slangy", "sledge", "sleepy", "sleety", "sleeve", "sleigh",
                     "slight", "slinky", "slippy", "sluice", "slushy", "smooth", "smudge", "smudgy",
                     "snaggy", "snazzy", "snoopy", "snoozy", "social", "socket", "sodium", "softie",
                     "solemn", "solids", "sonnet", "source", "sparky", "speech", "speedy", "sphere",
                     "sphinx", "spider", "spinet", "spiral", "spooky", "sporty", "spotty",
                     "sprain", "sprawl", "spring", "spruce", "sprung", "square", "squash",
                     "squish", "stable", "stagey", "stamen", "staple", "starch", "starry",
                     "static", "statue", "steady", "steely", "stereo", "stocks", "stocky",
                     "stolid", "stormy", "streak", "stride", "string", "stripe", "stripy", "stroll",
                     "strong", "stubby", "studio", "sturdy", "subtle", "suburb", "subway", "sudden",
                     "suffix", "sugary", "sulpha", "summer", "sundry", "sunken", "sunlit", "sunset",
                     "superb", "supine", "supper", "supply", "surfer", "surtax", "survey",
                     "swampy", "swanky", "sweaty", "switch", "swivel", "sylvan", "symbol",
                     "syntax", "syrupy", "tablet", "taking", "talent", "talker", "tangle", "tanker",
                     "tannic", "target", "tartan", "taster", "tavern", "teacup", "teapot", "teasel",
                     "temper", "tennis", "tester", "tether", "thesis", "thirty", "thrill", "throes",
                     "throne", "ticker", "ticket", "tiddly", "tiered", "tights", "timber", "timely",
                     "tinker", "tinned", "tinted", "tipped", "tipple", "tiptop", "tissue", "titchy",
                     "titled", "tomato", "tracer", "trader", "treaty", "treble", "tremor", "trendy",
                     "tricky", "triple", "troops", "trophy", "trough", "truant", "trusty", "tucker",
                     "tufted", "tundra", "tunnel", "turbid", "turkey", "turtle", "tussle", "twirly",
                     "twisty", "umlaut", "unable", "unborn", "undone", "uneven", "unique", "unlike",
                     "unmade", "unpaid", "unread", "unreal", "unsaid", "unseen", "unsold", "untold",
                     "unused", "unwary", "unworn", "upbeat", "uphill", "upland", "uproar", "uptake",
                     "upward", "upwind", "urbane", "urchin", "urgent", "usable", "useful", "utmost",
                     "valley", "vapour", "varied", "veggie", "veiled", "veined", "velour", "velvet",
                     "verbal", "verity", "vernal", "versed", "vertex", "vessel", "viable", "vinous",
                     "violet", "violin", "visage", "viscid", "visual", "volume", "voyage", "waders",
                     "waggle", "waiter", "waiver", "waking", "wallet", "wallop", "walrus", "wanted",
                     "warble", "warder", "wealth", "wearer", "webbed", "webcam", "wedded",
                     "weevil", "wheezy", "whippy", "wicker", "wifely", "wilful", "window",
                     "winged", "winger", "winner", "winter", "wintry", "witted", "wizard", "wobbly",
                     "wonder", "wonted", "wooded", "woolly", "worthy", "wreath",
                     "wrench", "yarrow", "yearly", "yellow", "yonder", "zapper", "zenith", "zigzag",
                     "zircon", "zither"]
        case 3:
            words = ["abiding", "ability", "abiotic", "absence", "account", "acidity",
                     "acrobat", "acrylic", "actress", "actuary", "adamant", "addenda", "address",
                     "advance", "aerated", "aerobic", "affable", "ageless", "airport", "alcopop",
                     "alleged", "amazing", "ambient", "amenity", "amiable", "amusing", "anaemia",
                     "ancient", "angelic", "angling", "angular", "animate", "animism", "aniseed",
                     "annular", "annulus", "anodyne", "antacid", "anthill", "antique",
                     "antonym", "aplenty", "apology", "apparel", "applied", "apropos", "aquatic",
                     "aqueous", "arbiter", "archaic", "article", "ascetic", "aseptic", "assured",
                     "athlete", "attache", "audible", "aureole", "autocue", "average", "avidity",
                     "awesome", "bagpipe", "balcony", "balloon", "bandsaw", "banquet", "bargain",
                     "baronet", "barrage", "bassist", "battery", "beeline", "belated", "beloved",
                     "bemused", "bequest", "bespoke", "betters", "bicycle", "billion", "binding",
                     "biology", "biscuit", "bismuth", "bivalve", "blanket", "blatant",
                     "blessed", "blister", "blogger", "blossom", "blowfly", "blurred", "bonfire",
                     "bookish", "boracic", "boulder", "boxroom", "boycott", "boyhood", "bracket",
                     "bravery", "breaded", "breadth", "breathy", "brimful", "brisket", "bristly",
                     "brittle", "bromide", "brother", "buckram", "bucolic", "budding", "builder",
                     "bulrush", "bulwark", "buoyant", "burning", "bursary", "butcher", "buzzard",
                     "cabaret", "cadence", "cadenza", "caisson", "calends", "calorie", "candied",
                     "cannery", "capable", "capital", "captain", "caption", "capture",
                     "caravan", "caraway", "carbide", "careful", "carmine", "carnage", "cartoon",
                     "carving", "cashier", "cavalry", "ceiling", "centaur", "central", "centric",
                     "century", "ceramic", "certain", "cession", "chamber", "channel", "chapter",
                     "charity", "charmer", "chatter", "checked", "checker", "chemist", "chevron",
                     "chicane", "chicken", "chimney", "chirrup", "chortle", "chuffed", "civvies",
                     "clarion", "classic", "clastic", "cleaver", "clement", "climate",
                     "clinker", "cluster", "clutter", "coastal", "coating", "coaxial", "cobbled",
                     "coequal", "cognate", "coldish", "collage", "college", "comical", "commune",
                     "compact", "company", "compass", "complex", "concave",
                     "concert", "concise", "conduit", "conical", "content", "contest", "control",
                     "convert", "cooking", "coolant", "copious", "copycat", "cordial", "coronet",
                     "correct", "council", "counter", "country", "courage", "courtly",
                     "crackle", "crawler", "crested", "crimson", "crinkly", "croquet", "crucial",
                     "crumbly", "crunchy", "cryptic", "crystal", "culvert", "cunning",
                     "cupcake", "curator", "curious", "currant", "current", "curried",
                     "cursive", "cursory", "curtain", "cushion", "customs", "cutaway",
                     "cutback", "cutlass", "cutlery", "cutting", "cyclist", "dabbler",
                     "dancing", "dappled", "darling", "dashing", "dawning", "deadpan", "decagon",
                     "decided", "decimal", "decoder", "defiant", "deltaic", "denizen",
                     "dentist", "dervish", "desktop", "dessert", "devoted", "devotee",
                     "diagram", "diamond", "dietary", "diffuse", "digital", "dignity",
                     "dioxide", "diploid", "diploma", "display", "distant", "disused", "diurnal",
                     "diverse", "divided", "dolphin", "donnish", "dormant", "doughty", "drachma",
                     "drastic", "draught", "drawing", "dresser", "dribble", "driving", "drought",
                     "drummer", "duality", "ductile", "dungeon", "duopoly", "durable", "dustbin",
                     "dutiful", "dynamic", "dynasty", "earmark", "earnest", "earplug", "earring",
                     "earshot", "earthen", "earthly", "eastern", "easting", "eclipse", "economy",
                     "edaphic", "egghead", "elastic", "elderly", "elegant", "elegiac",
                     "ellipse", "elusive", "emerald", "eminent", "emirate", "emotive",
                     "empties", "endemic", "endless", "engaged", "enquiry", "ensuing", "epicure",
                     "epigeal", "episode", "epitome", "equable", "equator", "equerry", "erosive",
                     "erudite", "eternal", "ethical", "evasive", "evening", "evident", "exalted",
                     "example", "excited", "exhaust", "exigent", "expanse", "express", "extreme",
                     "factual", "fairing", "fancier", "fantasy", "faraway", "fashion", "feather",
                     "feature", "federal", "feeling", "felspar", "ferrety", "ferrous", "ferrule",
                     "fervent", "festive", "fibrous", "fiction", "fighter", "figment", "filings",
                     "finicky", "fishnet", "fissile", "fission", "fitting", "fixated", "fixture", "flannel",
                     "flavour", "flecked", "fledged", "flighty", "flouncy", "flowery", "fluency",
                     "fluster", "fluvial", "foliage", "foliate", "footing", "footman", "forfeit",
                     "fortune", "forward", "fragile", "freckly", "freebie", "freeman",
                     "freesia", "freezer", "fretted", "friable", "frilled", "fringed", "frosted", "frowsty",
                     "fulsome", "furcate", "furlong", "furrier", "further", "furtive", "fusible", "fusilli",
                     "gainful", "gallant", "gallery", "gamelan", "garbled", "garnish", "gavotte",
                     "gazette", "gearbox", "general", "genteel", "genuine", "germane", "getaway",
                     "gherkin", "gibbous", "gingery", "giraffe", "girlish", "glaring", "gleeful",
                     "glimmer", "glowing", "gnomish", "goggles", "gorilla", "gradual", "grammar",
                     "grandam", "grandee", "graphic", "grating", "gravity", "greatly", "greyish",
                     "greylag", "gristly", "grocery", "grommet", "grooved", "gryphon", "guarded",
                     "guising", "gushing", "gymnast", "habitat", "hafnium", "halcyon", "halfway",
                     "hallway", "halogen", "halting", "halyard", "handbag", "harbour", "harvest",
                     "heading", "healthy", "hearing", "heating", "helical", "helpful", "helping",
                     "herbage", "heroics", "hexagon", "history", "hitcher", "holdall", "holiday",
                     "holmium", "hominid", "homonym", "honeyed", "hopeful", "horizon",
                     "hotline", "hotness", "hulking", "hunched", "hundred", "hurdler", "hurried",
                     "hydrous", "hygiene", "idyllic", "igneous", "immense", "imprint", "inbuilt",
                     "inexact", "infuser", "ingrown", "initial", "inkling", "inshore",
                     "instant", "intense", "interim", "invader", "inverse",
                     "isohyet", "isthmus", "italics", "jackpot", "jasmine", "jocular", "journal",
                     "journey", "jubilee", "justice", "kenning", "kestrel", "keynote", "kindred",
                     "kinetic", "kingdom", "kinsman", "kitchen", "knowing", "knuckle",
                     "knurled", "laconic", "lacquer", "lactose", "lagging", "lambent", "lantern",
                     "largish", "lasting", "lateral", "lattice", "lawsuit", "layette", "leading", "leaflet",
                     "learned", "learner", "leather", "lectern", "legible", "leisure", "lengthy",
                     "lenient", "leonine", "leopard", "lettuce", "lexical", "liberty", "library", "lilting",
                     "lineage", "linkage", "linkman", "lioness", "literal", "lithium", "logging",
                     "logical", "longish", "lottery", "louvred", "lovable", "lowland", "luggage",
                     "lyrical", "machine", "maestro", "magenta", "magical", "magnate",
                     "majesty", "maltose", "mammoth", "manners", "mansard",
                     "marbled", "marital", "marquee", "mascara", "massive", "matinee", "matting",
                     "mattock", "maximal", "maximum", "mayoral", "meaning",
                     "medical", "meeting", "melodic", "mermaid", "message", "midland",
                     "midweek", "million", "mimetic", "mindful", "mineral",
                     "minimal", "minimum", "minster", "missile", "missing", "mission", "mistake",
                     "mixture", "modular", "mollusc", "moneyed", "monitor", "monthly", "moonlit",
                     "moorhen", "morello", "morning", "mottled", "mounted", "mourner",
                     "movable", "muddler", "muffler", "mullion", "musical", "mustard",
                     "nankeen", "narwhal", "natural", "nebular", "needful", "neither", "netball",
                     "netting", "network", "newness", "nightly", "nitrous", "nomadic", "nominal",
                     "notable", "noughth", "nuclear", "nursery", "nursing", "nurture", "obesity",
                     "oblique", "obscure", "obvious", "oceanic", "octagon", "octopus", "offbeat",
                     "officer", "offline", "offside", "oilcake", "ominous", "onerous", "ongoing",
                     "onshore", "opening", "opinion", "optimal", "optimum", "opulent", "orbital",
                     "orchard", "ordered", "orderly", "ordinal", "organic", "osmosis",
                     "osmotic", "outdoor", "outline", "outside", "outsize", "outward",
                     "overall", "overarm", "overlay", "package", "padlock", "pageant", "painter",
                     "paisley", "palaver", "palette", "palmate", "palmtop", "panicle", "paragon",
                     "parking", "parlous", "partial", "passage", "passing", "passive", "pastime",
                     "pasture", "patient", "pattern", "payable", "peacock", "peckish",
                     "pelagic", "pelisse", "penalty", "pendent", "pending", "penguin", "pension",
                     "peppery", "perfect", "perfume", "persona", "phantom", "philtre", "phonics",
                     "picture", "piebald", "pillbox", "pinched", "pinkish", "piquant", "pitcher",
                     "pitfall", "pivotal", "plaster", "plastic", "platoon", "playful", "pleased",
                     "pleated", "plenary", "pliable", "plumber", "plunger", "podcast", "poetess",
                     "pointed", "polemic", "politic", "popcorn", "popular", "portion", "postage",
                     "postbox", "postern", "postman", "potable", "pottage", "pottery", "powdery",
                     "powered", "praline", "prattle", "precise", "prefect", "premier", "present",
                     "prickle", "primary", "process", "product", "profuse", "program",
                     "project", "pronged", "pronoun", "propane", "protean", "protein", "proverb",
                     "proviso", "prudent", "psychic", "puckish", "pumpkin", "purpose", "puzzler",
                     "pyjamas", "pyramid", "pyrites", "quality", "quantum", "quarter", "quavery",
                     "queenly", "quinine", "quorate", "rabbity", "rackety", "radiant", "radical",
                     "raffish", "rafting", "railing", "railman", "railway", "rainbow", "rambler",
                     "ramekin", "rampant", "rarebit", "ratable", "raucous", "rawhide", "readies",
                     "recital", "recount", "recruit", "redhead", "redwing", "referee", "refined",
                     "regards", "regatta", "regency", "regnant", "regular", "related", "relaxed",
                     "reliant", "remorse", "removed", "replete", "reproof", "reptile", "reputed",
                     "respect", "restful", "restive", "rethink", "retired", "retread", "revelry",
                     "revenge", "reverse", "rhombus", "rickety", "rimless", "ringing", "riotous",
                     "riviera", "roaring", "robotic", "rolling", "roseate", "rounded", "rounder",
                     "routine", "ruffled", "ruinous", "runaway", "rundown", "running",
                     "saddler", "sailing", "salient", "salvage", "sampler", "sapient", "sardine",
                     "saurian", "sausage", "savings", "savoury", "scarlet", "scenery", "scented",
                     "science", "scrappy", "scratch", "scrawny", "screech", "scribal", "sealant",
                     "searing", "seasick", "seaside", "seaward", "seaweed", "section", "secular",
                     "seedbed", "seeming", "segment", "seismic", "sensory", "sensual", "serious",
                     "serried", "servant", "several", "shadowy", "shapely", "shelter", "sheriff",
                     "shivery", "shocker", "showery", "showing", "shrubby", "shudder", "shutter",
                     "sickbay", "sidecar", "sighted", "sightly", "signing", "silvery", "similar",
                     "sincere", "sinless", "sinuous", "sixfold", "sketchy", "skilful", "skilled",
                     "skimmed", "skyline", "skyward", "slatted", "sleeved", "slipper", "slotted",
                     "slowish", "slurred", "sniffle", "sniffly", "snuffly", "snuggly", "society",
                     "soldier", "soluble", "someone", "soprano", "sorghum", "soulful", "spangle",
                     "spangly", "spaniel", "spanner", "sparing", "sparkly", "sparrow", "spartan",
                     "spatial", "speaker", "special", "speckle", "spidery", "spindly", "splashy",
                     "splotch", "spotted", "springy", "spurred", "squally", "squashy", "squidgy",
                     "squiffy", "squishy", "stadium", "standby", "stapler", "starchy",
                     "starlit", "stately", "station", "stature", "staunch", "stealth", "stellar", "sticker",
                     "stilted", "stoical", "strange", "stratum", "streaky", "stretch", "striker", "strings",
                     "stringy", "striped", "stubbly", "student", "studied", "stylish", "styptic",
                     "subject", "sublime", "success", "suiting", "sultana", "summary",
                     "summery", "sunburn", "sundial", "sundown", "sunfish", "sunless",
                     "sunrise", "sunroof", "support", "supreme", "surface", "surfeit",
                     "surgery", "surmise", "surname", "surplus", "surreal", "swarthy", "swearer",
                     "sweater", "swollen", "synapse", "synonym", "tabular", "tactful", "tactile",
                     "tadpole", "tallish", "tangram", "tantrum", "taxable", "teacher", "telling",
                     "tenable", "tenfold", "tensile", "ternary", "terrace", "terrain", "terrine", "testate",
                     "textile", "textual", "texture", "theatre", "thistle", "thought", "thrifty", "through",
                     "thrower", "thunder", "tideway", "timpani", "titanic", "titular", "toaster",
                     "toccata", "tombola", "tonight", "toothed", "topical", "topmost", "topsoil",
                     "torment", "tornado", "touched", "tourism", "tourist", "tracing", "tracker",
                     "tractor", "trailer", "trainer", "trapeze", "treacly", "tremolo", "triable", "triadic",
                     "tribune", "trickle", "trochee", "trolley", "trophic", "tropism", "trouble",
                     "trouper", "trumpet", "tsunami", "tubular", "tumbler", "tunable", "tuneful",
                     "twelfth", "twiddly", "twilled", "twitchy", "twofold", "typical", "umpteen",
                     "unaided", "unarmed", "unasked", "unaware", "unbound", "unbowed",
                     "uncanny", "undying", "unequal", "unheard", "unicorn", "unifier", "uniform",
                     "unitary", "unladen", "unlined", "unmoved", "unnamed", "unpaved",
                     "unready", "untried", "unusual", "unwaged", "upfront", "upright", "upriver",
                     "upstage", "upstate", "upswept", "useable", "utility", "valiant",
                     "vanilla", "variant", "variety", "various", "vaulted", "vehicle", "velvety",
                     "venison", "verbena", "verbose", "verdant", "verdict", "verdure", "vernier",
                     "version", "vesicle", "vibrant", "victory", "vinegar", "vintage", "vintner",
                     "virtual", "visible", "visitor", "vitamin", "vlogger", "volcano", "voltaic",
                     "voluble", "voucher", "vulpine", "waggish", "wagtail", "wakeful", "walkout",
                     "wallaby", "wanting", "warmish", "warrant", "washing", "waverer", "waxwing",
                     "waxwork", "wayward", "wealthy", "wearing", "weather",
                     "webbing", "website", "weighty", "welcome", "western", "wetsuit",
                     "wheaten", "wheelie", "whisker", "widower", "wildcat", "willing", "willowy",
                     "winning", "winsome", "wishful", "wistful", "witness", "woollen", "working",
                     "worldly", "worsted", "wriggly", "wrinkle", "writing", "wrought",
                     "zealous", "zestful"]
        case _:
            print('Invalid difficulty! Check your code!!')
            return False

    selected_word = choice(words)
    randomized_word = list(selected_word)
    shuffle(randomized_word)

    print(r'''
 _   _       _                 _     _      
| | | |_ __ (_)_   _ _ __ ___ | |__ | | ___ 
| | | | '_ \| | | | | '_ ` _ \| '_ \| |/ _ \
| |_| | | | | | |_| | | | | | | |_) | |  __/
 \___/|_| |_|_|\__,_|_| |_| |_|_.__/|_|\___|
''')
    print('Unjumble the given letters into a valid word!')
    print(f'Your letters are: {randomized_word}')
    while True:
        user_word = input('Enter the valid word: ').lower()
        if len(user_word) != len(randomized_word):
            print('Wrong length, try again!')
            continue
        num_valid_letters = 0
        for i in user_word:
            if i in randomized_word:
                num_valid_letters += 1
        if num_valid_letters != len(randomized_word):
            print('You entered the wrong letters, try again!')
            continue
        if user_word in words:
            print(f'You won! The word was indeed {user_word}!')
            return True
        print(f'You lose! The word was {selected_word}. Better luck next time!')
        return False

def game_find_the_cats(diff):
    match diff:
        case 0:
            x = 3
            y = 3
        case 1:
            x = 4
            y = 4
        case 2:
            x = 5
            y = 5
        case 3:
            x = 6
            y = 6
        case _:
            print('Invalid case!')
            return False

    num_cards = randint(1, (x*y)//2)
    cards = [[x*i+j for j in range(1, x+1)] for i in range(y)]
    cards_1 = [i for i in range(3, x*y+1)]
    cats = []
    for i in range(num_cards):
        ch = choice(cards_1)
        cats.append(ch)
        cards_1.remove(ch)
    del cards_1

    print(r'''
  ____      _   _____ _           _           
 / ___|__ _| |_|  ___(_)_ __   __| | ___ _ __ 
| |   / _` | __| |_  | | '_ \ / _` |/ _ \ '__|
| |__| (_| | |_|  _| | | | | | (_| |  __/ |   
 \____\__,_|\__|_|   |_|_| |_|\__,_|\___|_|   ''')
    print('Find the cats, they will be marked with a \U0001f431 emoji!')
    print('Your cards are given below, you have 5 seconds to memorize their positions!')
    for i in cards:
        for j in i:
            if j in cats:
                print('[\U0001f431]', end='')
            else:
                print('[ ]', end='')
        print()
    for i in range(y*2, 0, -1):
        print(f'{i}...', end=' ')
        sleep(1)
    print()
    for i in range(100):
        print('\n'*10)

    selected_cards = []
    selected_card = 0
    while True:
        for i in cards:
            for j in i:
                if j in selected_cards:
                    print('[\u2705]', end='')
                else:
                    print(f"[{'' if j // 10 > 0 else ' '}{j} ]", end='')
            print()
        try:
            selected_card = int(input('Enter the number on the card with a cat: '))
            if selected_card in cats:
                selected_cards.append(selected_card)
            else:
                for i in cards:
                    for j in i:
                        if j == selected_card:
                            print('[\u274c]', end='')
                        elif j in selected_cards:
                            print('[\u2705]', end='')
                        else:
                            print(f"[{'' if j // 10 > 0 else ' '}{j} ]", end='')
                    print()
                print('The card didn\'t have a cat, you lose! Better luck next time!')
                return False
            if set(selected_cards) == set(cats):
                for i in cards:
                    for j in i:
                        if j in selected_cards:
                            print('[\u2705]', end='')
                        else:
                            print(f"[{'' if j // 10 > 0 else ' '}{j} ]", end='')
                    print()
                print('You win! You got all cards correct!')
                return True
        except Exception:
            print('Enter a valid card number.')

def guess_the_number(diff):
    print(r'''
  _   _                 _                  ____                     
 | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___ 
 | \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/''')
    print('Very Hot -> Less than 3 away from the right number')
    print('Hot -> Less than 5 away from the right number')
    print('Warm -> Less than 7 away from the right number')
    print('Cold -> Less than 10 away from the right number')
    print('Very Cold -> More than 10 away from the right number')

    limit = 0
    match diff:
        case 0:
            print('You have to guess the number between 1 and 20.')
            limit = 20
        case 1:
            print('You have to guess the number between 1 and 50.')
            limit = 50
        case 2:
            print('You have to guess the number between 1 and 80.')
            limit = 80
        case 3:
            print('You have to guess the number between 1 and 100.')
            limit = 100

    rand_no = randint(1, limit)
    max_guesses = int(limit**0.5)

    for i in range(max_guesses):
        while True:
            try:
                guess = int(input('Enter your guess: '))
                if guess not in range(1, limit+1):
                    print(f'Please enter your guess within the limits (1 to {limit})!')
                else:
                    break
            except Exception:
                print('Please enter a proper value!')

        if guess == rand_no:
            print(f'You win! The number was {rand_no}!')
            return True
        else:
            dist = int(abs(guess - rand_no))
            if dist < 3:
                print('\u2728 Very hot')
            elif dist < 5:
                print('\U0001f525 Hot')
            elif dist < 7:
                print('\U0001f321 Warm')
            elif dist < 10:
                print('\U0001f9ca Cold')
            else:
                print('\u2744 Very cold')

    print(f'The number was {rand_no}. Better luck next time!')
    return False
