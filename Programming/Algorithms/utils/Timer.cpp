#include "Timer.h"
void Timer::reset()
{
  begin = Clock::now();
}
double Timer::elapsed() const
{
  return std::chrono::duration_cast<Second>(Clock::now() - begin).count();
}
