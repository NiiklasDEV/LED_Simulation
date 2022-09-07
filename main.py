import pygame
from abc import ABC, abstractmethod
import time


class GPIODevice:
    pins = []

    def __init__(self, pin: int, value: bool) -> None:
        self.pin = pin
        self.value = value

    @property
    def pin(self):
        return self.pin

    @property
    def value(self):
        return self.value

    @pin.setter
    def pin(self, value):
        self._pin = value

    @value.setter
    def value(self, value):
        self._value = value


class OutputDevice(GPIODevice):
    def __init__(self, pin: int, value: bool, active_high: bool) -> None:
        super().__init__(pin, value)

    def off(self):
        self.led.off()

    def on(self):
        self.led.on()

    def toggle(self):
        self.led = True

    @property
    def active_high(self):
        return self.active_high

    @active_high.setter
    def active_high(self, value):
        self._active_high = value


class DigitalOutputDevice(GPIODevice):
    def __init__(self, pin: int, value: bool) -> None:
        super().__init__(pin, value)

    def blink(self, on_time: float, off_time: float, n: int):
        OutputDevice.led.on()
        time.sleep(on_time)
        OutputDevice.led.off()
        time.sleep(off_time)


class Observer(ABC):
    def __init__(self) -> None:
        super().__init__()

        @abstractmethod
        def update(self, device: GPIODevice):
            pass


class LED(DigitalOutputDevice, Observer):
    def __init__(self, pin: int, value: bool) -> None:
        super().__init__(pin, value)
        self.observer = []
        background_colour = (0, 0, 0)
        pygame.init()
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 300
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.fill(background_colour)
        pygame.display.flip()
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def add_observer(self, new_observer: Observer):
        self.observer.append(new_observer)
        new_observer.update(self)

    def update(self, device: GPIODevice):
        # Add that the bool for Ison is true and if so it will turn on the LED
        pass
