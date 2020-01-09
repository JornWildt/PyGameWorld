class SceneBuilder:
    def build_scene1(scene, sprites):
        scene_src = '''
XXXXXXXXXXXX
x..........X
x..........X
x......XXXXX
x..........X
x.....B....X
x..........X
x..........X
x..........X
XBBBBB***XXX
x....b....BX
x..........X
x....B.....X
x...b....b.X
x........b.X
x..........X
xxxxxxxxxxxx
'''

        scene_src_x = '''
XXX
B.X
BBX
'''

        scene.load_scene_from_string(scene_src, sprites)
