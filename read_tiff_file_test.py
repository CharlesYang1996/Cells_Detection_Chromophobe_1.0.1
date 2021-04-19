import openslide
from pylab import *
import numpy
import pylab
import time
start_time = time.clock()
slide = openslide.OpenSlide('H:/test1.tiff')

#层数
level_count = slide.level_count
print ('level_count = ',level_count)

[m,n] = slide.dimensions #得出高倍下的（宽，高）(97792,219648)
print (m,n)


#显示目标区域
tile = numpy.array(slide.read_region((50000,40000),0, (1200,1000)))
plt.figure()
plt.imshow(tile)
pylab.show()



slide_level_downsamples = slide.level_downsamples[2]

slide_downsamples = slide.get_best_level_for_downsample(5.0)

#tile = numpy.array(slide.read_region((0,0),6, (1528,3432)))

from openslide.deepzoom import DeepZoomGenerator
#图像扫描仪制造商
print(slide.detect_format('H:/test1.tiff'))

#幻灯片的各种属性
print(slide.properties)


end_time = time.clock()

print('Running time: %s Seconds'%(end_time-start_time))