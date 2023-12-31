# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Messages

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Drinks(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Drinks()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDrinks(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Drinks
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Drinks
    def Cans(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Messages.Cans import Cans
            obj = Cans()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Drinks
    def Bottles(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Messages.Bottles import Bottles
            obj = Bottles()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def DrinksStart(builder):
    builder.StartObject(2)

def Start(builder):
    DrinksStart(builder)

def DrinksAddCans(builder, cans):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(cans), 0)

def AddCans(builder, cans):
    DrinksAddCans(builder, cans)

def DrinksAddBottles(builder, bottles):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(bottles), 0)

def AddBottles(builder, bottles):
    DrinksAddBottles(builder, bottles)

def DrinksEnd(builder):
    return builder.EndObject()

def End(builder):
    return DrinksEnd(builder)
