import WorldGenerator
import GameComponents

generator = WorldGenerator.WorldGenderator()

world = generator.generateWorld(5,5, seed =0)
#world.printAllRooms(world.currentRoom)

for i in range(0,20):

    enemy = GameComponents.Enemy()
    enemy.randomizeEnemy(i)

    enemy.printEnemyInfo()
