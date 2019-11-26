<?xml version="1.0" encoding="UTF-8"?>
<project name="RaceCarControls" board="Mojo V3" language="Lucid">
  <files>
    <src>steering.luc</src>
    <src>analoginputs.luc</src>
    <src top="true">mojo_top.luc</src>
    <src>acceleration.luc</src>
    <ucf lib="true">io_shield.ucf</ucf>
    <ucf lib="true">mojo.ucf</ucf>
    <component>spi_slave.luc</component>
    <component>uart_rx.luc</component>
    <component>cclk_detector.luc</component>
    <component>reset_conditioner.luc</component>
    <component>avr_interface.luc</component>
    <component>uart_tx.luc</component>
    <component>counter.luc</component>
  </files>
</project>
