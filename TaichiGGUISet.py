"""
The setting of the taichi ggui
"""

def gui_set(pos, target, FOV=60):
    # init the window, canvas, scene and camerea
    window = ti.ui.Window("XPBD", (1080, 720), vsync=True)
    scene = ti.ui.Scene()
    camera = ti.ui.Camera()

    # initialize camera position
    camera.position(pos[0], pos[1], pos[2])
    camera.lookat(target[0], target[1], target[2])
    camera.fov(FOV)

    # set the camera, you can move around by pressing 'wasdeq'
    camera.track_user_inputs(window, movement_speed=0.03, hold_key=ti.ui.RMB)
    scene.set_camera(camera)

    # set the light
    scene.point_light(pos=(0, 1, 3), color=(1., 1., 1.))
    scene.point_light(pos=(0, 0, 3), color=(1., 1., 1.))
    scene.ambient_light((0.7, 0.7, 0.7))
    return window, camera, scene


def gui_show(window, canvas, scene, SHOW_FLAG=True):
    """
    Show the GUI
    """
    if SHOW_FLAG is False:
        return
    # the conversion of object particles, etc. the ggui of the taichi only support float32
    particle_show_np = particle_field.pos.to_numpy(dtype=np.float32)
    particle_show.from_numpy(particle_show_np)
    top_particle_show.from_numpy(top_field.pos.to_numpy(dtype=np.float32))

    scene.mesh(particle_show, indices=surf_show, color=(1, 1, 0))
    scene.particles(top_particle_show, radius=0.002, color=(0, 1, 1))
    canvas.scene(scene)
    # window.save_image(f'png/{n}.png')
    window.show()
