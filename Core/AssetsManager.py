import pyganim
import json
import os
from .Rendering.SpriteSheet import SpriteSheet

class AssetsManager:
    def get(self, name):
        return self.assets[name]
        

    def load_from_directory(self, dir):
        self.assets = {}
        self.assets_dir = dir

        with open(dir + "/assets.json", encoding='utf-8-sig') as assets_file:
            assets_json = json.load(assets_file)

            for name in assets_json:
                asset = assets_json[name]
                if asset["type"] == "animation":
                    animation = self.load_animation(asset["file"], asset["rows"], asset["cols"])
                    self.assets[name] = animation
                if asset["type"] == "spritesheet":
                    self.load_spritesheet(asset["file"], asset["content"])


    def load_animation(self, file, rows, cols):
        images = pyganim.getImagesFromSpriteSheet(os.path.join(self.assets_dir, file), rows=rows, cols=cols, rects=[])
        # TODO: customizable delay
        frames = list(zip(images, [100] * len(images)))
        anim = pyganim.PygAnimation(frames)
        anim.play()
        return anim

    # def load_spritesheets(self, assets_json):
    #     for name in assets_json:
    #         asset = assets_json[name]
    #         if asset["type"] == "spritesheet":
    #             self.load_spritesheet(asset["file"], asset["content"])


    def load_spritesheet(self, file, content):
        sheet = SpriteSheet(os.path.join(self.assets_dir, file))
        for sprite_name in content:
            if sprite_name in self.assets:
                raise NameError("Repeated sprite name: " + sprite_name)
            sprite = self.load_sprite_from_sheet(sheet, content[sprite_name])
            self.assets[sprite_name] = sprite

        # pyganim.getImagesFromSpriteSheet("Assets/Random/Ghost3D.png", rows=1, cols=1, rects=[])


    def load_sprite_from_sheet(self, sheet, sprite_content):
        if sprite_content["type"] == "image":
            position = sprite_content["position"]
            image = sheet.image_at(position)
            return image
        else:
            raise NameError("Undefined asset type: " + sprite_content["type"])
