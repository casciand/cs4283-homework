# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Messages

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Veggies(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Veggies()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVeggies(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Veggies
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Veggies
    def Tomato(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Veggies
    def Cucumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def VeggiesStart(builder):
    builder.StartObject(2)

def Start(builder):
    VeggiesStart(builder)

def VeggiesAddTomato(builder, tomato):
    builder.PrependFloat32Slot(0, tomato, 0.0)

def AddTomato(builder, tomato):
    VeggiesAddTomato(builder, tomato)

def VeggiesAddCucumber(builder, cucumber):
    builder.PrependFloat32Slot(1, cucumber, 0.0)

def AddCucumber(builder, cucumber):
    VeggiesAddCucumber(builder, cucumber)

def VeggiesEnd(builder):
    return builder.EndObject()

def End(builder):
    return VeggiesEnd(builder)