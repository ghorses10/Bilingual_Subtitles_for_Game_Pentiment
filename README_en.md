## [Patch] [v1.0] [Pentiment] Bilingual Subtitles for Game Pentiment

<h4 align="center">
    <p>
        <a href="README.md">中文</a> | <b>English</b>
    <p>
</h4>

This is a bilingual subtitles patch designed for the game "Pentiment".



### 免责声明/Disclaimer

Please carefully read and understand the following disclaimer before using this patch. By installing, using, or otherwise obtaining this patch, you agree to comply with the following provisions:

1. This patch is based on the official translation. The author of this patch (hereinafter referred to as the "author") holds the copyright, and it cannot be reproduced or used for commercial purposes without authorization. Any derivative works using this patch must explicitly credit the author.

2. This patch is intended for personal entertainment purposes only. The author is not responsible for any direct or indirect losses or damages resulting from the use of this patch.

3. This patch may modify the original content of the game, including but not limited to text, images, and sounds. The use of this patch may cause abnormal or unstable game functionality. The author is not responsible for any issues caused by the use of this patch.

4. This patch may not be compatible with certain updates or other patches of the game. The author is not responsible for problems arising from conflicts with game updates or other patches.

5. **Please ensure that you back up your game data before using this patch.** The author is not responsible for any data loss caused by the use of this patch.

   

### 简介/Introduction

This patch enables bilingual subtitles within the game.

With this patch, you can:

- Enjoy bilingual subtitles to avoid misunderstandings caused by translation errors; it may also aid in learning English (lol).
- Resolve the issue of lacking distinctive fonts, providing an authentic and original experience..
- The patch also includes a Python program for generating bilingual subtitles. You can create your own subtitles according to your preferences.

The effects of this patch are illustrated in the following image: 

![ (1)](photo/(1).png)

![ (5)](photo/(5).png)

![ (4)](photo/(4).png)



### 下载/Download

The "patch" folder contains bilingual subtitle files for various languages.



### 使用教程/Tutorial

The tutorial is divided into two steps. The first step involves using a Python program to generate personalized bilingual subtitles. The second step is to import these subtitles into the game. If you don't need to make personalized modifications to the bilingual patch, you can skip the first step and proceed directly to the second step, using the bilingual patch files provided by the author.



#### 生成属于自己的双语字幕/Generate your own bilingual subtitles

**依赖/Requirement：**

- python 3.8.0
- chardet 5.2.0

Implementation: Concatenate translated subtitles with English subtitles.

Place the original English subtitle file, translated subtitle file, and the corresponding program in the same folder. Modify the file names according to the comments in the program. Then, run the program, and you will obtain the created bilingual subtitle file named `output.stringtablebundle` !



#### 安装补丁/Install Patch

Rename the bilingual subtitle file (if you followed the first step, it would be the output file `output.stringtablebundle`; if downloaded directly from the website, it would be the downloaded file `text_xxxx.stringtablebundle`) to `text_enus.stringtablebundle`. Copy this file to `<Pentiment installation directory>/Pentiment_Data/StreamingAssets/localized/enus/text`, overwriting the original file to complete the installation.

After installation, launch the game and choose English as the language to enable bilingual subtitles!



### 已知Bug/Bug

After applying this patch, making manual modifications to the English subtitles may result in misalignment of characters (to be corrected).

![ (6)](photo/(6).png)




