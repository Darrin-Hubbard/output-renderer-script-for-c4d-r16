import c4d

bc = c4d.GetMachineFeatures()
print bc[c4d.OPENGL_RENDERER_NAME]