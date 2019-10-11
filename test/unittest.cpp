#include <gmock/gmock.h>

#include "logger/logger.h"

namespace
{
	class Mock
	{
	public:
		MOCK_METHOD0(Function, void());
	};
}

TEST(Logger, CanConstructAndDestruct)
{
   Logger log;
}

TEST(Logger, CanLogMessage)
{
   Logger().Log("Message");
}

TEST(Logger, CanUseMocks)
{
	Mock mock;
	EXPECT_CALL(mock, Function());

	mock.Function();
}

