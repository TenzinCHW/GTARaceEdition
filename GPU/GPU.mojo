<?xml version="1.0" encoding="UTF-8"?>
<project name="GPU" board="Mojo V3" language="Lucid">
  <files>
    <src>filtershape.luc</src>
    <src>matmul.luc</src>
    <src>matvecmul.luc</src>
    <src>dotprod.luc</src>
    <src>split.luc</src>
    <src top="true">mojo_top.luc</src>
    <ucf lib="true">io_shield.ucf</ucf>
    <ucf lib="true">mojo.ucf</ucf>
    <component>reset_conditioner.luc</component>
  </files>
</project>
