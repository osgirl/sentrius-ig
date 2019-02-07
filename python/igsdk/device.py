#
# device.py
#
# Device API for Laird Industrial Gateway
#

import dbus
import dbus.exceptions
import logging

DEVICE_SERVICE='com.lairdtech.device.DeviceService'
DEVICE_SERVICE_OBJ_PATH='/com/lairdtech/device/DeviceService'
DEVICE_SERVICE_PUBLIC_IFACE='com.lairdtech.device.public.DeviceInterface'

DEVICE_ERR_INVALID = -1
DEVICE_ERR_UNINIT = -2

def device_init():
    """Initialize the IG device API
    Returns:
        Device instance, to be used in device_* calls
    """
    try:
        ret = dbus.Interface(dbus.SystemBus().get_object(DEVICE_SERVICE,
            DEVICE_SERVICE_OBJ_PATH), DEVICE_SERVICE_PUBLIC_IFACE)
        return ret
    except dbus.exception.DBusException as e:
        logging.getLogger(__name__).error('Cannot open Device interface: {}'.format(e))
        return None

def device_enabled(dev):
    if dev:
        dev.DeviceEnabled()

def device_activity(dev):
    if dev:
        dev.DeviceActivity()

def device_exception(dev):
    if dev:
        dev.DeviceException()

def set_serial_port_type(dev, port_type):
    if dev:
        return dev.SetSerialPortType(port_type)
    else:
        return DEVICE_ERR_UNINIT

def set_serial_termination(dev, term):
    if dev:
        return dev.SetSerialTermination(term)
    else:
        return DEVICE_ERR_UNINIT

