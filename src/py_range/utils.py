from random import choice

# words
prefix = choice([
    'appy', 'old', 'rave', 'keen', 'wise', 'soft', 'rude',
    'zany', 'mad', 'raw', 'jam', 'gay', 'few', 'vex',
    'blue', 'dry', 'wry', 'icy', 'sun', 'dim',
    'red', 'big', 'wet', 'hot', 'cold', 'warm', 'cool',
    'frosty', 'gentle', 'quick', 'slow', 'brave',
    'bold', 'calm', 'free', 'wild', 'prim',
])
metals = [
    'iron', 'gold', 'silver', 'copper', 'bronze',
    'steel', 'tin', 'lead', 'zinc', 'nickel',
    'chrome', 'platinum', 'titanium', 'tungsten',
    'electrum', 'mithril', 'adamantite', 'orichalcum',
    'cobalt', 'magnesium', 'aluminum', 'mercury',
    'palladium', 'rhodium', 'iridium', 'osmium',
    'ruthenium', 'gallium', 'indium', 'bismuth',
    'tantalum', 'hafnium', 'vanadium', 'scandium',
    'boron', 'silicon', 'germanium', 'arsenic',
    'antimony', 'tellurium', 'polonium', 'francium',
    'radium', 'actinium', 'thorium', 'protactinium',
]
nouns = [
    'badger', 'fox', 'wolf', 'eagle', 'hawk', 'owl', 'bear',
    'lion', 'tiger', 'dragon', 'phoenix', 'raven', 'crow',
    'otter', 'seal', 'whale', 'shark', 'squid', 'crab',
    'beetle', 'ant', 'bee', 'wasp', 'fly', 'moth',
    'fern', 'moss', 'vine', 'oak', 'pine', 'cedar', 'fir',
    'rock', 'stone', 'cliff', 'dune', 'sand', 'snow',
    'spark', 'flare', 'glow', 'beam', 'ray', 'wave',
    'river', 'lake', 'ocean', 'stream', 'brook', 'pond',
    'storm', 'rain', 'wind', 'mist', 'fog', 'hail',
    'leaf', 'bloom', 'petal', 'thorn', 'root', 'seed',
]

def random_name() -> str:
    return f"{prefix}-{choice(metals)}-{choice(nouns)}"

