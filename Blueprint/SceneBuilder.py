class SceneBuilder:
    def build_scene1(scene, sprites):
        scene_src = '''
XXXXXXXXXXXX
x..........X
x..........X
x..........X
x..........X
x..........X
XXXXXXXX*XXX
x...b.....BX
x...b......X
x..........X
x...bbb..b.X
x........b.X
x..........X
xxxxxxxxxxxx
'''

        scene.load_scene_from_string(scene_src, sprites)
