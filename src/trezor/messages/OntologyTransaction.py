# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .OntologyTxAttribute import OntologyTxAttribute

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class OntologyTransaction(p.MessageType):

    def __init__(
        self,
        version: int = None,
        type: int = None,
        nonce: int = None,
        gas_price: int = None,
        gas_limit: int = None,
        payer: str = None,
        tx_attributes: List[OntologyTxAttribute] = None,
    ) -> None:
        self.version = version
        self.type = type
        self.nonce = nonce
        self.gas_price = gas_price
        self.gas_limit = gas_limit
        self.payer = payer
        self.tx_attributes = tx_attributes if tx_attributes is not None else []

    @classmethod
    def get_fields(cls):
        return {
            1: ('version', p.UVarintType, 0),
            2: ('type', p.UVarintType, 0),
            3: ('nonce', p.UVarintType, 0),
            4: ('gas_price', p.UVarintType, 0),
            5: ('gas_limit', p.UVarintType, 0),
            6: ('payer', p.UnicodeType, 0),
            7: ('tx_attributes', OntologyTxAttribute, p.FLAG_REPEATED),
        }
