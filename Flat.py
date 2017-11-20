from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
air = 0
stone = 1
grass = 2
dirt = 3
cobblestone = 4
wood_planks = 5
sapling = 6
bedrock = 7
water_flowing = 8
water = 8
water_stationary = 9
lava_flowing = 10
lava = 10
lava_stationary = 11
sand = 12
gravel = 13
gold_ore = 14
iron_ore = 15
coal_ore = 16
wood = 17
leaves = 18
glass = 20
lapis_lazuli_ore = 21
lapis_lazuli_block = 22
sandstone = 24
bed = 26
cobweb = 30
grass_tall = 31
wool = 35
flower_yellow = 37
flower_cyan = 38
mushroom_brown = 39
mushroom_red = 40
gold_block = 41
iron_block = 42
stone_slab_double = 43
stone_slab = 44
brick_block = 45
tnt = 46
bookshelf = 47
moss_stone = 48
obsidian = 49
torch = 50
fire = 51
stairs_wood = 53
chest = 54
diamond_ore = 56
diamond_block = 57
crafting_table = 58
farmland = 60
furnace_inactive = 61
furnace_active = 62
door_wood = 64
ladder = 65
stairs_cobblestone = 67
door_iron = 71
redstone_ore = 73
snow = 78
ice = 79
snow_block = 80
cactus = 81
clay = 82
sugar_cane = 83
fence = 85
glowstone_block = 89
bedrock_invisible = 95
stone_brick = 98
glass_pane = 102
melon = 103
fence_gate = 107
glowing_obsidian = 246
nether_reactor_core = 247
def init(): 
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def main():
	mc = init()
	mc.player.setPos(0, 0, 0)
	x, y, z = mc.player.getPos()  
	mc.player.setPos(x, y, z)
	mc.setBlocks(x-256, y, z-256, x+256, y+63, z+256, air)
	
main()

"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD PLANKS           5
SAPLING               6
BEDROCK               7
WATER FLOWING         8
WATER                 8
WATER STATIONARY      9
LAVA FLOWING         10
LAVA                 10
LAVA STATIONARY      11
SAND                 12
GRAVEL               13
GOLD ORE             14
IRON ORE             15
COAL ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS LAZULI ORE     21
LAPIS LAZULI BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS TALL           31
WOOL                 35
FLOWER YELLOW        37
FLOWER CYAN          38
MUSHROOM BROWN       39
MUSHROOM RED         40
GOLD BLOCK           41
IRON BLOCK           42
STONE SLAB DOUBLE    43
STONE SLAB           44
BRICK BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS WOOD          53
CHEST                54
DIAMOND ORE          56
DIAMOND BLOCK        57
CRAFTING TABLE       58
FARMLAND             60
FURNACE INACTIVE     61
FURNACE ACTIVE       62
DOOR WOOD            64
LADDER               65
STAIRS COBBLESTONE   67
DOOR IRON            71
REDSTONE ORE         73
SNOW                 78
ICE                  79
SNOW BLOCK           80
CACTUS               81
CLAY                 82
SUGAR CANE           83
FENCE                85
GLOWSTONE BLOCK      89
BEDROCK INVISIBLE    95
STONE BRICK          98
GLASS PANE          102
MELON               103
FENCE GATE          107
GLOWING OBSIDIAN    246
NETHER REACTOR CORE 247
"""
