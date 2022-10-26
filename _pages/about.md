---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

崔丰麒,男,2001年11月生,合肥工业大学微电子科学与工程专业大三在读.我目前在情感计算与先进智能机器安徽省重点实验室[MAC-Lab](http://faculty.hfut.edu.cn/sunxiao/zh_CN/index.htm)团队助研、在中国科学技术大学先进技术研究院（合肥综合性国家科学中心人工智能研究院）[普适心理计算实验室](http://iai.ustc.edu.cn/iai/r271.html)实习,师从[孙晓](http://faculty.hfut.edu.cn/sunxiao/zh_CN/index.htm)教授.我的主要研究方向为：情感计算、普适心理计算与交互干预技术的研究与应用 等.  

我目前的具体研究领域为：多模态情绪协同感知与交互干预技术在交通安全、驾驶行为、智能座舱等车载场景下的应用.截至目前,我受理专利3项,主持国家级大学生创新创业训练计划项目一项,以团队第一主持人带队获得第八届中国国际“互联网+”大学生创新创业大赛国家级银奖一项，获各类教育部竞赛排行榜赛事国家级2项、省部级/市级8项、校级若干.作为法人注册“晓声智能科技股份有限公司”,专注于
情感智能座舱领域技术的研究与应用,目前项目纳入合肥市种子项目基金库、获得合肥市科创委5万余元创业基金并于合肥工业大学智能制造技术研究院进行企业孵化,并受邀参加深度学习技术与工程应用国家实验室与百度飞桨联合举办的[ Wave Summit2022+ 峰会](https://www.wavesummit.com.cn/)展览,并于合肥工业大学智能制造技术研究院、合肥工业大学微电子学院等多个单位进行[路演汇报与经验分享](http://news.hfut.edu.cn/info/1017/51049.htm).

# 🔥 News
- *2022.09*: &nbsp;🎉🎉  第1届合肥工业大学“智能杯”创新创业大赛 二等奖（5万元创业基金）（团队负责人）.  
- *2022.08*: &nbsp;🎉🎉  2022年”建行杯”第8届中国国际”互联网+”大学生创新创业大赛 安徽省省级金奖 并入围国家级总决赛 （团队负责人）.  

# 📖 Educations
- *2020.06 - now*, 合肥工业大学,微电子学院,微电子科学与工程专业，本科三年级在读. 


# 📝 Scientific Research 
我目前在情感计算与先进智能机器安徽省重点实验室[MAC-Lab](http://faculty.hfut.edu.cn/sunxiao/zh_CN/index.htm)团队助研、在中国科学技术大学先进技术研究院（合肥综合性国家科学中心人工智能研究院）[普适心理计算实验室](http://iai.ustc.edu.cn/iai/r271.html)实习,我们的团队总负责人为[汪萌](http://faculty.hfut.edu.cn/wm12/zh_CN/index.htm)教授（国家杰青、IEEE Fellow、IAPR Fellow）,我的指导老师是[孙晓](http://faculty.hfut.edu.cn/sunxiao/zh_CN/index.htm)教授.我的主要研究方向为：情感计算、普适心理计算与交互干预技术的研究与应用 等.我目前的具体研究领域为：多模态情绪协同感知与交互干预技术在交通安全、驾驶行为、智能座舱等车载场景下的应用.截至目前,我受理专利3项,主持国家级大学生创新创业训练计划项目一项.    

- *2022.4* 发明专利受理——基于并行复用的卷积神经网络的硬件加速器及并行复用方法.<br>本发明公开了一种基于并行复用的卷积神经网络的硬件加速器及并行复用方法，该硬件加速器包括：参数存储模块、REG‑FIFO模块、计数控制模块、输入复用的卷积运算模块、激活模块、池化层模块；其中，参数存储模块负责预存图片参数和练后的权值参数；REG‑FIFO模块负责生成与卷积核相匹配的输入矩阵以及读取矩阵数据；计数控制模块负责时钟周期计数并依此控制REG‑FIFO模块的输入输出；输入复用的卷积运算模块负责卷积层与全连接层的卷积运算；激活模块负责卷积层和全连接层的输出激活操作；池化层模块负责经激活后的卷积层输出的池化操作。本发明旨在实现高运算并行度、高度数据复用、低硬件复杂度的卷积神经网络计算.  
- *2022.4* 一种基于操作数裁剪的高性能近似乘法器及其计算方法.<br>本发明公开了一种基于操作数裁剪的高性能近似乘法器及其计算方法，该近似乘法器包括：部分积生成模块、部分积树形压缩模块、进位加法器模块和移位模块；部分积生成模块包括操作数裁剪模块和位乘积模块，操作数裁剪模块对乘数和被乘数进行截取操作，得到近似操作数，位乘积模块得到相应的部分积；部分积树形压缩模块用于得到最终求和的两个加数；进位加法器模块用于最终两个加数相加，移位模块用于对进位加法器模块的输出进行移位，得到所求的二进制结果。本发明能够极大程度降低多位乘法器的面积、延时和功耗，同时也能保持较好的精确度.
- *2022.5* 国家级大创项目立项——基于多模态情感计算与FPGA硬件加速的车载心理干预系统.<br>针对因“路怒症”等危险驾驶状态引发的道路交通事故起数呈逐年上升，中国司机心理障碍的发生率高等社会问题；与完善智能汽车生态建设体系，构建具有良好人机交互功能的情感智能座舱等企业需求，团队通过整合中国科学技术大学先进技术研究院普适心理计算团队、合肥工业大学情感计算与先进智能机器安徽省重点实验室软硬件相关的优势资源，开发出了一套结合了边缘端硬件加速与多模态情感计算的车载嵌入式情绪识别与心理干预系统，可实现通过无接触式采集驾驶员的微表情、心电等多模态信号进行实时的情绪分类，并及时对危险心理状态进行干预，为驾驶员的行车安全与心理健康保驾护航.

# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 


# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
