# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Messages

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Bottles(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Bottles()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBottles(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Bottles
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Bottles
    def Sprite(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def BottlesStart(builder):
    builder.StartObject(1)

def Start(builder):
    BottlesStart(builder)

def BottlesAddSprite(builder, sprite):
    builder.PrependInt32Slot(0, sprite, 0)

def AddSprite(builder, sprite):
    BottlesAddSprite(builder, sprite)

def BottlesEnd(builder):
    return builder.EndObject()

def End(builder):
    return BottlesEnd(builder)
