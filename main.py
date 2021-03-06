"""
Title : crusade
Creators : Chandler Varney and Jackson Clark
Description : You're a Knight going on a crusade to kill the dragon
"""
#Make the player, camera, and controls
Knight = sprites.create(img("""
    ......cccccc....
    .....cbbbbbbc...
    ..ccccbbccccccc.
    .ceeecbbc2b2b2c.
    ceeeecbbcb2b2bc.
    ceeeecbbccccccc.
    ceeeecbbbbbbc...
    ceeeeeccccccc...
    ceeeeeeeeeeec...
    ceeeeecccccc....
    ceeeecbbbbbbc...
    ceeeecbbbbbbc...
    cebbecbbbbbbc.bb
    .cbbecbbbbbbc.bb
    .cbbecbbbbbbc.bb
    ..ceecbbbbbbc...
    ...ccccccccc....
    ................
    .....cc....cc...
    .....cc....cc...
"""),SpriteKind.player)
controller.move_sprite(Knight, 75, 0)
scene.camera_follow_sprite(Knight)
Knight.ay = 275
can_jump = True
def jump():
    global can_jump
    if can_jump:
        Knight.vy= -100
        can_jump = Knight.is_hitting_tile(CollisionDirection.BOTTOM)
controller.up.on_event(ControllerButtonEvent.PRESSED, jump)
info.player1.set_life(1)
game.show_long_text("Welcome to the crusade 1.3 update AKA rags and riches! We've added a bunch more items! Have fun, Dev",DialogLayout.BOTTOM)
game.show_long_text("You have fallen into an dungeon full of evilmonsters.You must throw your swords(spacebar) and move with the arrow keys to defeat them. There are also a few treasures hidden around. Find them for the secret ending. Enjoy!", DialogLayout.BOTTOM)
info.set_score(0)

#Make the level
scene.set_tile_map(img("""
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    b6.................................................................................................b
    b..................................................................................................b
    b..................................................................................................b
    b..................................................................................................b
    b..................................................................................................b
    b...................................................bb2bb..........................................b
    b.................................................................bbbbbb2bbbbbb2bbbbbbbbbbbbbbbbb..b
    b.............................bbbbbbbbbb.........................bb................................b
    bbbbbbbbb...................bb..........b.......................bb.................................b
    b....................bbb2bbb.............b.....................bb..................................b
    b...................b.....................b2bbbbbbbbbbbbbbbbb2bb..............................b2bb.b
    b.............bbbbbb...............................................................................b
    b............b.....................................................................................b
    b...........b........................................................................bbbb2b........b
    b..........b......................................................bbb2bbbbbbbbbb2b.................b
    b.........b...................................bbbbbbbbbbbbbbbb.....................................b
    bb2bbbbbb....................................bb...............bb...................................b
    b....................bb22bbbb22b.bbbbbbbbbbb2b..................bb.................................b
    b........b...........b6........b..................................bbbbbbbbbbbbb....................b
    b.........b...bbbbb..b.........bb..............................................2bbbbbbbbbbb2.......b
    b..........b.........b.........bbb.............................................b6..........bbbb....b
    b...........b........b.........b.bb............................................b...........b.......b
    b...........bbbbbbb..b.........b..bb...........bbbbbb2bbbb2bbbbbb..b...........b...........b....bbbb
    b...................bb.........b.bb............b................b..b...........b..........4b.......b
    b..................bbb.........bbb....bbbbbbbb.b................b..b...bbbb....b..bbbbbbbbbbbbb....b
    b.......bbbbbbbbbbbbbb...bbbbbbbb....bb6.......b....bbbbbbbbbbbbb..b...........b..................bb
    b......bb............bb.............b.........bbb.............................bbb................bb.
    b....bbb..............bb...........b...........bbb..........................bbb.bb..............bb..
    bbbbbb.................bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb2bbbbb2b....bbbbbbb2bbbbbbbb...
"""))
scene.set_tile(11, img("""
    f f f f f f f f f f f f f f f f
    f c c c c c f c c c c c c c c f
    f c c c c c f f f f c c c c c f
    f c c c c c f c c f c c c c c f
    f f f f f f f c c f f f f f f f
    f c c c f c c c c f c c f c c f
    f c c c f c c c c f c c f c c f
    f c c c f f f f f f c c f c c f
    f c c c c c c f c c c c f f c f
    f c c c c c c f c c c c c f c f
    f f f f f f f f c c c c c f c f
    f c c c c f c f c c c c c f f f
    f c c c c f c f f f f f f f c f
    f c c c c f c c c c c c c c c f
    f c c c c f c c c c c c c c c f
    f f f f f f f f f f f f f f f f
"""),True)
scene.set_tile(6, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . 5 . . . . . . .
    . . . . . . . 5 . . . . . . . .
    . . . . . . . . 5 . . . . . . .
    . . . . . . . 5 4 5 . . . . . .
    . . . . . . f 5 4 5 f . . . . .
    . . . . . . . f f f . . . . . .
    . . . . . . . . e . . . . . . .
    . . . . . . . . e . . . . . . .
    . . . . . . . . e . . . . . . .
    . . . . . . . . f . . . . . . .
    e e e e e e e f e . . . . . . .
    . . . . . . . f e . . . . . . .
    . . . . . . . . f . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
scene.set_tile(5, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . 5 5 5 . . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . 5 5 f 5 5 . . . . . .
    . . . . . 5 5 f 5 5 . . . . . .
    . . . . . 5 5 f 5 5 . . . . . .
    . . . . . 5 5 f 5 5 . . . . . .
    . . . . . 5 5 f 5 5 . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . . 5 5 5 . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
scene.set_tile(14, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . e e e e e e e e e . . .
    . . . . e e e e e e e e e . . .
    . . . . e f f f 5 f f f e . . .
    . . . . e f f f 5 f f f e . . .
    . . . . e e e e e e e e e . . .
    . . . . e e e e e e e e e . . .
"""))
scene.set_tile(2, img("""
    . . . . . . . . . . . . . . . .
    . 1 1 . 1 1 . 1 1 . 1 1 . 1 1 .
    1 2 2 1 2 2 1 2 2 1 2 2 1 2 2 1
    f f f f f f f f f f f f f f f f
    f c c c f c c c c c f c c c c c
    f c c c f c c c c c f c c c c c
    f c c c f f f f f f f f f c c c
    f c c c f c c f f c c c f f f f
    f f f f f c c f c c c c f c c c
    f c c f c c c f c c c c f c c c
    f c c f c c c f f f f f f f f f
    f c c f f f f f c f c c c c c c
    f c c c c c c c c f c c c c c c
    f c c c c c c c c f c c c c c c
    f c c c c c c c c f c c c c c c
    f f f f f f f f f f f f f f f f
"""),True)
scene.set_tile(4, img("""
    a a a a a a a a a a a a a a a a
    a 8 a 8 8 8 8 8 8 8 8 8 8 8 8 a
    a 8 a a a a 8 8 8 8 8 8 8 8 a a
    a 8 8 8 8 a 8 8 a a a 8 8 8 a a
    a 8 8 8 8 a 8 8 a 8 a a a a a a
    a 8 8 8 8 a 8 8 a 8 8 8 8 8 8 a
    a 8 8 8 8 a a a a 8 8 8 8 8 8 a
    a 8 8 8 8 8 a a a a a a a 8 8 a
    a 8 8 8 8 a a a a 8 8 8 a 8 8 a
    a 8 8 8 8 8 8 a 8 8 8 8 a 8 8 a
    a 8 8 8 8 8 8 a 8 8 8 8 a 8 8 a
    a 8 8 8 8 a a a 8 8 8 8 a 8 8 a
    a 8 8 8 a a 8 8 8 8 8 a a 8 8 a
    a 8 a a a 8 8 8 8 8 8 a a 8 8 a
    a a a 8 8 8 8 8 8 8 8 a 8 8 8 a
    a a a a a a a a a a a a a a a a
"""))

#Make life losing system
def on_hit_tile(sprite):
    scene.camera_shake(15)
    info.change_life_by(-1)
scene.on_hit_tile(SpriteKind.player, 2 , on_hit_tile)

# Make the projectiles
def on_button_event_a_pressed():
    projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . c c c c c c c . . .
        . . . . . c 1 1 1 1 1 1 1 c . .
        . . . c c 2 1 1 1 1 1 1 1 1 c .
        . . . . . c 1 1 1 1 1 1 1 c . .
        . . . . . . c c c c c c c . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), Knight, 70, 0)
    projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . c c c c c c c . . . . .
        . . . c 1 1 1 1 1 1 1 c . . . .
        . . c 1 1 1 1 1 1 1 1 2 c c . .
        . . . c 1 1 1 1 1 1 1 c . . . .
        . . . . c c c c c c c . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), Knight, -70, 0)
controller.player1.on_button_event(ControllerButton.A, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)

# make double jump
def on_update():
    global can_jump
    if Knight.is_hitting_tile(CollisionDirection.BOTTOM):
        can_jump = True
game.on_update(on_update)

#make enemy
voodoo_skull = sprites.create(img("""
    . . . . 2 2 2 2 2 2 2 . . . . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . 2 2 2 2 2 2 2 2 2 2 2 . . .
    . . 2 2 2 2 2 2 2 2 2 2 2 . . .
    . . 2 2 2 1 2 2 2 1 2 2 2 . . .
    . . 2 2 1 2 1 2 1 2 1 2 2 . . .
    . . 2 2 2 1 2 2 2 1 2 2 2 . . .
    . . 2 2 2 2 2 1 2 2 2 2 2 . . .
    . . 2 2 2 2 1 2 1 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . . . 2 2 2 2 2 2 2 . . . . .
    . . . . . 2 1 2 1 2 . . . . . .
    . . . . . 2 1 2 1 2 . . . . . .
    . . . . . 2 2 2 2 2 . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.enemy)
voodoo_skull.follow(Knight, 50)
jesters_mask = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . f f f f f 2 2 2 2 2 . . .
    . . f f f f f 2 f 2 2 2 2 2 . .
    . . f f 2 2 f f 2 2 f f 2 2 . .
    . . f f 2 2 f 2 f 2 f f 2 2 . .
    . . f f 2 2 f f 2 2 f f 2 2 . .
    . . f f 2 2 f 2 f 2 f f 2 2 . .
    . . f f 2 2 f f 2 2 f f 2 2 . .
    . . f f 2 2 f 2 f 2 f f 2 2 . .
    . . f f f f f f 2 2 2 2 2 2 . .
    . . . f f f f 2 f 2 2 2 2 . . .
    . . . . . f f f 2 2 2 . . . . .
    . . . . . f f 2 f 2 2 . . . . .
    . . . . . f f f 2 2 2 . . . . .
    . . . . . . . . . . . . . . . .
    """),SpriteKind.enemy)
jesters_mask.follow(Knight,35)
lost_one = sprites.create(img("""
    . . . 4 . . . . . 2 . 4 4 . . .
    . . 4 2 . 4 4 4 4 4 . 4 . . 4 .
    . . 4 4 4 2 4 4 4 4 2 4 . 2 . .
    . . 4 4 4 4 4 4 4 4 4 4 4 . . .
    . . 2 4 2 2 2 2 2 2 2 4 4 . . .
    . . 4 2 2 2 2 2 2 2 2 2 4 . . .
    . . 4 2 2 2 2 5 2 2 2 2 2 . . .
    . . 2 2 1 1 1 2 1 1 1 2 5 . . .
    . . 5 2 1 1 1 2 1 1 1 2 2 . . .
    . . 2 2 1 1 1 5 1 1 1 5 2 . . .
    . . 2 5 5 5 5 5 5 5 5 5 5 . . .
    . . 5 5 5 5 1 1 1 5 5 5 5 . . .
    . . 5 5 5 1 5 5 5 1 5 5 5 . . .
    . . . 5 5 5 5 5 5 5 5 5 . . . .
    . . . . 5 5 5 5 5 5 5 . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.enemy)
lost_one.follow(Knight, 40)
yes = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . c c c c . . c c c c . . .
    . . c . . . . . . . . . . c . .
    . c . . . a a a a a a . . . c .
    . c . . a c c c c c c a . . c .
    . c . a c c c c c c c c a . c .
    . c . a c c c c c c c c a . c .
    . c . a c c c c c c c c a . c .
    . c . a c c c c c c c c a . c .
    . c . a c c c c c c c c a . c .
    . c . a c c c c c c c c a . c .
    . c . . a c c c c c c a . . c .
    . c . . . a a a a a a . . . c .
    . . c . . . . . . . . . . c . .
    . . . c c c c . . c c c c . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.enemy)
yes.follow(Knight , 55)
my_sprite2 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . 2 2 2 2 2 2 2 . . . .
    . . . . 2 2 1 2 2 1 1 1 2 . . .
    . . . 2 2 1 1 1 2 1 1 1 2 2 . .
    . . 2 2 2 1 1 1 2 1 1 1 2 2 2 .
    . . 2 2 2 1 1 1 2 1 1 1 2 2 2 .
    . . 2 2 2 1 1 1 2 1 1 1 2 2 2 .
    . . 2 2 2 1 2 1 2 1 1 1 2 2 2 .
    . . 2 2 2 2 2 2 2 2 2 2 2 2 2 .
    . . 2 2 1 2 2 2 2 2 2 2 1 2 2 .
    . . 2 2 1 1 1 1 1 1 1 1 1 2 2 .
    . . . 2 2 1 1 1 1 1 1 1 2 2 . .
    . . . . 2 2 1 1 1 1 1 2 2 . . .
    . . . . . 2 2 2 2 2 2 2 . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))

#Make the damage and stuff
def on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap)
def on_overlap3(sprite, otherSprite):
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap3)

# Make the coins
gem = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . f f f f f f f f f f . . .
    . . f 9 9 9 9 9 9 9 9 9 9 f . .
    . f 9 1 1 9 9 9 9 9 9 1 9 9 f .
    f 9 9 1 9 9 9 9 9 9 9 9 9 9 9 f
    . f 9 9 9 9 9 9 9 9 9 9 9 9 f .
    . . f 9 9 9 9 9 9 9 1 9 9 f . .
    . . . f 9 9 9 9 9 9 1 9 f . . .
    . . . . f 9 9 9 1 1 9 f . . . .
    . . . . . f 9 9 9 9 f . . . . .
    . . . . . . f 9 9 f . . . . . .
    . . . . . . . f f . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.food)
coin = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . 5 1 1 5 5 5 5 . . . . .
    . . . . 5 1 5 f 5 5 5 . . . . .
    . . . . 5 5 5 f 5 5 5 . . . . .
    . . . . 5 5 5 f 5 1 5 . . . . .
    . . . . 5 5 5 f 5 5 5 . . . . .
    . . . . 5 5 5 f 5 5 5 . . . . .
    . . . . 5 5 5 f 5 5 5 . . . . .
    . . . . 5 5 5 5 1 5 5 . . . . .
    . . . . . 5 5 5 5 5 . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.food)
gem2 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . a a a a a a . . . . .
    . . . . a a a a a a a a . . . .
    . . . a a 1 1 c c c c a a . . .
    . . . a c 1 c c c c c c a . . .
    . . . a c c c c c c c 1 a . . .
    . . . a c c c c c c c 1 a . . .
    . . . a a c c c c 1 1 a a . . .
    . . . . a a a a a a a a . . . .
    . . . . . a a a a a a . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.food)
amulet = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 5 5 5 5 5 5 5 . . . .
    . . . . 5 . . . . . . . 5 . . .
    . . . 5 . . . . . . . . . 5 . .
    . . . 5 . . . . . . . . . 5 . .
    . . . 5 . . . . . . . . . 5 . .
    . . . . 5 . . . . . . . 5 . . .
    . . . . . 5 . . . . . 5 . . . .
    . . . . . . 5 . . . 5 . . . . .
    . . . . . . . 5 . 5 . . . . . .
    . . . . . . . . 5 . . . . . . .
    . . . . . . . 1 1 1 . . . . . .
    . . . . . . 1 1 2 1 1 . . . . .
    . . . . . . . 1 1 1 . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.food)
ruby = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . 2 2 2 . . . . . . .
    . . . . . 2 2 2 2 2 . . . . . .
    . . . . 2 2 1 1 2 2 2 . . . . .
    . . . 2 2 1 1 2 2 2 2 2 . . . .
    . . . 2 2 1 2 2 2 2 2 2 . . . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . . 2 2 2 2 2 2 1 2 2 . . . .
    . . . 2 2 2 2 2 1 1 2 2 . . . .
    . . . . 2 2 2 2 2 2 2 . . . . .
    . . . . . 2 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.food)
money_bag = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . d d d d d d . . . . .
    . . . . d d d d d d d d f . . .
    . . . . f f f f f f f f . . . .
    . . . . . d d d d d d . f . . .
    . . . . . d d f f d d . . . . .
    . . . . d d f 5 5 f d d . . . .
    . . . d d f 5 5 5 5 f d d . . .
    . . d d d f 5 5 5 5 f d d d . .
    . . d d d f 5 5 5 5 f d d d . .
    . . d d d f 5 5 5 5 f d d d . .
    . . d d d f 5 5 5 5 f d d d . .
    . . d d d d f 5 5 f d d d d . .
    . . . d d d d f f d d d d . . .
    . . . . d d d d d d d d . . . .
"""),SpriteKind.food)
my_sprite = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
def on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
      info.player1.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap2)

#set stuff places
tiles.place_on_tile(jesters_mask, tiles.get_tile_location(54, 15))
tiles.place_on_tile(gem, tiles.get_tile_location(54, 13))
tiles.place_on_tile(coin, tiles.get_tile_location(26, 23))
tiles.place_on_tile(gem2, tiles.get_tile_location(54, 25))
tiles.place_on_tile(ruby, tiles.get_tile_location(85, 22))
tiles.place_on_tile(amulet, tiles.get_tile_location(1, 14))
tiles.place_on_tile(voodoo_skull, tiles.get_tile_location(43, 6))
tiles.place_on_tile(lost_one, tiles.get_tile_location(6, 23))
tiles.place_on_tile(yes, tiles.get_tile_location(93, 16))
tiles.place_on_tile(money_bag, tiles.get_tile_location(4, 24))
#Make the minimap


#Make an end to level one and a beginning to level two
def on_overlap_tile(sprite, location):
    pass
    scene.on_overlap_tile(SpriteKind.player, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), on_overlap_tile)

