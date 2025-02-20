#http://codecombat.com/play/level/diamond-dozen

#ADVICE - use fast sword


# Claim the coins while defeating the marauding ogres.
# If you defeat the ogre with the most health, the rest of the ogres will run!
# Coins vanish quickly after appearing, so be sure to find the best value!

def findMostHealth(enemies):
    target = None
    targetHealth = 0
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health
        enemyIndex += 1
    return target

# Make a function named findOptimalCoin which returns the coin with the best value.
# Coins rapidly appear and disappear, so pick the best coin.
# Optimize your path by going for the coin with the largest value over distance.
def findOptimalCoin(coins):
    optimal = -1000
    thione = None
    for coin in coins:
        if coin.value/self.distanceTo(coin)>optimal:
            optimal = coin.value/self.distanceTo(coin)
            thione = coin
    return thione

while True:
    enemies = hero.findEnemies()
    enemy = findMostHealth(enemies)
    if enemy and enemy.health > 15:
        while enemy.health > 0:
            hero.attack(enemy)
            hero.wait(2)
    else:
        coins = hero.findItems()
        coin = None
        coin = findOptimalCoin(coins) # ∆ Uncomment this once you've written the function.
        if coin:
            if hero.isReady('jump'):
                hero.jumpTo(coin)
            else:
                hero.moveXY(coin.pos.x, coin.pos.y)

