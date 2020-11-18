from experimental.db_models.base_models import *


class AlcatelServicePort(alcatel_base):
    __tablename__ = 'alcatelserviceport'
    id = Column(Integer(), primary_key=True)
    name = Column(String(64))
    box_id = Column(Integer, ForeignKey('alcatelbox.id'))
    connected_id = Column(Integer(), nullable=False)
    connected_type = Column(Enum('port', 'ont', 'cpe'), nullable=False)

    # Alcatel data
    pvid = Column(Integer(), default=None, nullable=True)
    max_unicast_mac = Column(Integer(), default=None, nullable=True)
    qos_profile_id = Column(Integer(), default=None, nullable=True)
    pvc = Column(Boolean(), default=False)
    admin_state = Column(Enum('0', '1', '2'), default='0')  # Alcatel: 0 => down, 1 => up, 2 => not-appl; Huawei: 0 => down, 1 => up
    operational_state = Column(Enum('0', '1'), default='0')  # Alcatel: 0 => down, 1 => up; Huawei: 0 => down, 1 => up
