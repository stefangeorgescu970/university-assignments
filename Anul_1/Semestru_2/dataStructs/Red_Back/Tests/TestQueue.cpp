//
// Created by Georgescu Stefan on 02/06/2017.
//

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "../DataStructures/Queue/Queue.h"
#include "../Exceptions/RedBackException.h"

using testing::Eq;

namespace {
    #include <string>
    class TestQueue : public testing::Test {
    public:
        TestQueue(){
        }
    };
}

TEST_F(TestQueue, test_queue_is_full){
    Queue my_queue{2};
    my_queue.push("Blue");
    ASSERT_EQ(my_queue.is_full(), false);
    my_queue.push("Red");
    ASSERT_EQ(my_queue.is_full(), true);
}

TEST_F(TestQueue, test_queue_is_empty){
    Queue my_queue{2};
    my_queue.push("Blue");
    ASSERT_EQ(my_queue.is_empty(), false);
    my_queue.pop();
    ASSERT_EQ(my_queue.is_empty(), true);
}

TEST_F(TestQueue, test_queue_push) {
    Queue my_queue{2};
    my_queue.push("Blue");
    my_queue.push("Red");
    ASSERT_EQ(my_queue.top(), "Blue");
    ASSERT_THROW(my_queue.push("Green"), QueueOverflowException);
    ASSERT_EQ(my_queue.pop(), "Blue");
}

TEST_F(TestQueue, test_queue_pop){
    Queue my_queue{2};
    my_queue.push("Blue");
    my_queue.push("Red");
    ASSERT_EQ(my_queue.pop(), "Blue");
    ASSERT_EQ(my_queue.pop(), "Red");
    ASSERT_THROW(my_queue.pop(), QueueUnderflowException);
}

TEST_F(TestQueue, test_queue_top){
    Queue my_queue{2};
    my_queue.push("Blue");
    ASSERT_EQ(my_queue.top(), "Blue");
    my_queue.pop();
    ASSERT_THROW(my_queue.top(), QueueUnderflowException);
}


