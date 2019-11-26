<?xml version="1.0" encoding="UTF-8"?>
<project name="GPU" board="Mojo V3" language="Lucid">
  <files>
    <src>matmul.luc</src>
    <src>matvecmul.luc</src>
    <src>dotprod.luc</src>
    <src top="true">mojo_top.luc</src>
    <ucf lib="true">mojo.ucf</ucf>
    <component>reset_conditioner.luc</component>
    <component>pipeline.luc</component>
    <component>button_conditioner.luc</component>
    <component>edge_detector.luc</component>
  </files>
</project>
