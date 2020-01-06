class SceneBuilder:
    def build_scene1(scene, sprites):
        scene_src = '''
XXXXXXXXXXXX
x..........X
x.....B....X
x..........X
x..........X
x..........X
XXX**XX**XXX
x....b....BX
x..........X
x..........X
x...b....b.X
x........b.X
x..........X
xxxxxxxxxxxx
'''

        scene.load_scene_from_string(scene_src, sprites)
