#include <gmock/gmock.h>

#include "logger.h"

TEST(Logger, CanConstructAndDestruct)
{
   FAIL("Boo");
   Logger log;
}
