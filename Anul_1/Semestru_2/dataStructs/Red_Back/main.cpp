#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "Game/Game.h"
#include "Exceptions/RedBackException.h"
#include "UserInterface/UserInterface.h"


using namespace std;

int main(int argc, char** argv) {

//    system("find . -name \"*.gcda\" -print0 | xargs -0 rm");

    testing::InitGoogleTest(&argc, argv);
    RUN_ALL_TESTS();

    UserInterface my_user_interface{};

    my_user_interface.run();

    return 0;
}


