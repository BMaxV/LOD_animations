from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class Wrapper:
    def __init__(self):

        # this is required for this demo
        self.b = ShowBase()

        # this is sort of optional allows for easily building and deleting
        # elements
        self.setup()

    def setup(self):

        # Load the environment model.
        # Reparent the model to render.
        scene = self.b.loader.loadModel("models/environment")
        scene.reparentTo(self.b.render)
        
        # Apply scale and position transforms on the model.
        scene.setScale(0.25, 0.25, 0.25)
        scene.setPos(-2, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.b.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
   
        # gltf doesn't work?
        self.load_example()
        self.load_example2()
        #self.load_pandas()
    
    def load_example2(self):
        self.load_example("./testing_lod_fine.gltf",off=2)
    
    def load_example(self,filename = "./testing1.gltf",off=0):
        print(filename)
        #filename = "./testing1.gltf"
        my_actor = Actor(filename)
        my_actor.reparentTo(self.b.render)
        my_actor.setScale(1,1,1)
        my_actor.setPos(-1 + off,0,2)
        
        names = my_actor.getAnimNames()
        print(names)
        
        name = names[0]
        print(name)
        
        my_actor.setPlayRate(1,name)
        my_actor.loop(name)
        
    def load_pandas(self):
        #regular panda
        regular_panda = Actor('panda-model', {
                            'walk': 'panda-walk4',
                            })
                            
        regular_panda.reparentTo(self.b.render)
        
        
    def spinCameraTask(self, task):
        d=20
        angleDegrees = task.time * 15.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.b.camera.setPos(d * sin(angleRadians), -d * cos(angleRadians), d)
        self.b.camera.setHpr(angleDegrees, -40, 0)

        return Task.cont


if __name__=="__main__":
    W=Wrapper()
    while True:
        W.b.taskMgr.step()
