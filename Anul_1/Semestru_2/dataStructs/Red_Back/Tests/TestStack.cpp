//
// Created by Georgescu Stefan on 02/06/2017.
//

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "../DataStructures/Stack/Stack.h"
#include "../Exceptions/RedBackException.h"

using testing::Eq;

namespace {
    #include <string>
    class TestStack : public testing::Test {
    public:
        Stack my_stack;
        TestStack() : my_stack{2} {
            my_stack.push("Blue");
        }
    };
}

TEST_F(TestStack, test_stack_top){
    ASSERT_EQ(my_stack.top(), "Blue");
    my_stack.pop();
    ASSERT_THROW(my_stack.top(), StackUnderflowException);
}

TEST_F(TestStack, test_stack_push){
    ASSERT_EQ(my_stack.top(), "Blue");
    my_stack.push("Red");
    ASSERT_EQ(my_stack.top(), "Red");
    ASSERT_THROW(my_stack.push("Green"), StackOverflowException);
}

TEST_F(TestStack, test_stack_pop){
    ASSERT_EQ(my_stack.pop(), "Blue");
    ASSERT_THROW(my_stack.pop(), StackUnderflowException);
}

TEST_F(TestStack, test_stack_is_empty){
    ASSERT_EQ(my_stack.is_empty(), false);
    my_stack.pop();
    ASSERT_EQ(my_stack.is_empty(), true);
}

TEST_F(TestStack, test_stack_is_full){
    ASSERT_EQ(my_stack.is_full(), false);
    my_stack.push("Red");
    ASSERT_EQ(my_stack.is_full(), true);
}
