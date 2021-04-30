# Blender-Gcode-Importer
G-code importer with some extra functionalities to convert from G-code to Blender mesh.  
Having access to the toolspaths directly let's you do some interesting things conventional slicers can't do.  
I've been using the importer in conjunction with <a href="https://github.com/alessandro-zomparelli/gcode-exporter">Alessandro Zomparelli's Gcode exporter</a> for Blender. It can also be used to get a preview of translucent prints.

<img src=https://raw.githubusercontent.com/Heinz-Loepmeier/wiki-sources/main/gcode-importer-docs/import.gif>

## Set up

### Compatibility

This add-on works on Blender 2.8.

Tested with G-code from _Slic3r_ and _Cura_. All G1 and G0 commands with an E-value get drawn as an edge. (Travel lines get omitted)

### Install

 1. Download this repo as a ZIP (Code > Download ZIP)
 1. Blender > Preferences > Add-ons > Install… > Select ZIP
 1. Enable the plugin (save preferences if you want this to be done by default)

## Usage

Once enabled, the _Properties_ sidebar (shortcut `N`) of the _3D Viewport_ will have a new tab called "Gcode Import" (see animated screencap above).

Options during importing:

  - **Subdivide**: Splits longer travel distances into multiple parts. For some Blender operations it helps if the paths are evenly segmentized to give some modifiers the necessary resolution.
  - **Split into layers**: Create one object per layer instead of a single Blender object.

You can find some more examples <a href="https://github.com/Heinz-Loepmeier/Blender-Gcode-Import/wiki">in the wiki.</a> (16MB of .gifs)
