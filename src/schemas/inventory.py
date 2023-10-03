from pydantic import BaseModel
import datetime as _dt


class _InventoryBase(BaseModel):
    ProductID: int
    InventoryChangeType: str
    QuantityChange: int
    CurrentInventoryQuantity: int
    InventoryUpdateDateTime : _dt.datetime
    LowStockThreshold : int
    PersonResponsibleID : str
    Notes : str



class InventoryCreate(_InventoryBase):
    pass

class Inventory(_InventoryBase):
    RecordID : int
 