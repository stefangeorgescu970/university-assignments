#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <vector>
#include <thread>

using namespace cv;

inline int convertToInt(char *s) {
  std::string _s(s);
  std::stringstream str(_s);
  int x;
  str >> x;
  if(!str || x <= 0) {
    return -1;
  }
  return x;
}

inline void displayImage(Mat &image) {
  namedWindow("Display Image", WINDOW_OPENGL);
  imshow("Display Image", image);
  waitKey(0);
}

int main(int argc, char** argv ) {
  clock_t t;
  t = clock();
  if (argc != 3 && argc != 4) {
    printf("Usage: GrayscaleFilter.o <Image_Path> <Number_of_threads> <generate_photo_size_n>\n");
    return -1;
  }
  std::string filename = argv[1];
  int N;
  int T = convertToInt(argv[2]);
  if(T == -1) {
    printf("Please give me a valid integer for the number of threads\n");
    return -1;
  }
  Mat image;
  if (argc == 3) {
    printf("Applying grayscale filter to %s\n", filename.c_str());
    image = imread(argv[1], cv::IMREAD_COLOR);
    if (!image.data) {
      printf("No image data\n");
      return -1;
    }
  } else if(argc == 4) {
    N = convertToInt(argv[3]);
    printf("Generating %d by %d matrix\n", N, N);
    image = Mat(N, N, CV_8UC3);
  }
  printf("Started working...\n");
  std::vector <std::thread> th;
  for(int t = 0; t < min(image.rows, T); ++ t) {
    th.push_back(std::thread([&image, t, T](){
      for(int i = t; i < image.rows; i += T) {
        for(int j = 0; j < image.cols; ++ j) {
          Vec3b px = image.at<Vec3b>(i, j);
          px[0] = 255 - px[0];
          px[1] = 255 - px[1];
          px[2] = 255 - px[2];
          image.at<Vec3b>(i, j) = px;
        }
      }
    }));
  }
  for(int i = 0; i < th.size(); ++ i) {
    th[i].join();
  }
  imwrite("negative.jpg", image);
//  displayImage(image);
  t = clock() - t;
  std::cout << "Applying grayscale filter to an image of "
      << image.rows << "x" << image.cols << " with " << T
      << " threads took me " << t << " cycles ("
      << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";
  std::cout << "Saved on negative.jpg\n";
  return 0;
}