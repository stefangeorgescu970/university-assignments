'use strict';

import React, {Component} from 'react';
import {
    StyleSheet,
    Text,
    View,
    FlatList,
    TouchableHighlight,
} from 'react-native';
import Swipeout from 'react-native-swipeout';
import {MyStatusBar} from '../Misc/MyStatusBar.js';
import {ServerTaskService} from '../Services/ServerTaskService.js';
import AddTaskModal from '../AddEditModals/AddTaskModal.js';
import EditTaskModal from '../AddEditModals/EditTaskModal.js';

class TaskListItem extends Component {
    constructor(props) {
        super(props);
        this.service = new ServerTaskService();
        this.state = {
            activeRowKey: null,
            numRefresh: 0
        };
    }

    getDateFormatted(dateParam) {
         var monthNames = [
            "January", "February", "March",
            "April", "May", "June", "July",
            "August", "September", "October",
            "November", "December"];

            var date = new Date(dateParam);

            var day = date.getDate();
            var monthIndex = date.getMonth();
            var year = date.getFullYear();

            return day + ' ' + monthNames[monthIndex] + ' ' + year;
    }

    refreshItem() {
        this.props.parentFlatList.refreshList();
    }

    render() {
        const swipeSettings = {
            autoClose: true,
            onClose: (secId, rowId, direction) => {
                this.setState({ activeRowKey: null });
            },
            onOpen: (secId, rowId, direction) => {
                this.setState({ activeRowKey: this.props.item.id });
            },
            right: [
                {
                    onPress: () => {
                        this.props.parentFlatList.refs.editModal.showEditModal(this.props.item, this);
                    },
                    text: 'Edit', type: 'primary'
                },
                {
                    onPress: () => {
                        const deletingRow = this.state.activeRowKey;
                        this.service.deleteTask(this.props.item, (success) => {
                            if (success == false) {
                                this.props.parentFlatList.deleteTask(this.props.item);
                            }
                        });
                    },
                    text: 'Delete', type: 'delete'
                }
            ],
            left: [
                {
                    onPress: () => {
                        const completedRow = this.state.activeRowKey;
                        this.service.completeTask(this.props.item, (success) => {
                            if (success == true) {
                                this.props.parentFlatList.refreshList();
                            }
                        });
                    },
                    text: 'Complete', type: 'primary'
                }
            ],
            rowId: this.props.index,
            sectionId: 1
        };
    return (

        <Swipeout {...swipeSettings}>
            <View style={styles.listCell}>

                <View style = {styles.listItemTitleHolder}>
                    <Text style={styles.listItemTitle}>{this.props.item.name}</Text>
                </View>

                <View style={styles.listItemSubtitleHolder}>

                    <View style={styles.listItemLeftSubtitleHolder}>
                        <Text style={styles.listItemSubtitleLeft}>{this.getDateFormatted(this.props.item.dueDate)}</Text>
                    </View>

                    <View style={styles.listItemRightSubtitleHolder}>
                        <Text style={styles.listItemSubtitleRight}>{this.props.item.project.name}</Text>
                    </View>

                </View>

                <View style={styles.listSeparator}>

                </View>

            </View>

        </Swipeout>
    );}
}

export default class TaskListPage extends Component<{}> {

    constructor(props) {
        super(props);
        this.service = new ServerTaskService();
        this.state = ({
            tasks: [],
        });

        this.refreshList();
        this.onPressAdd = this.onPressAdd.bind(this);
    }

    deleteTask(oldTask) {
        this.refreshList();
    }

    addNewTask(newTask) {
        var newTasks = this.state.tasks;
        newTasks.push(newTask);
        console.log(newTasks);
        this.setState({tasks: newTasks});
    }

    refreshList() {
        this.service.getTasks(false, (receivedTasks) => {
            console.log("Got tasks on list page " + receivedTasks);
            this.setState({tasks: receivedTasks});
        })
    }

    onPressAdd() {
        this.refs.addModal.showAddModal();
    }

    render() {
        return(
            <View style={{flex: 1}}>
                <MyStatusBar backgroundColor="#4C4C4C" barStyle="light-content" />

                <View style={styles.listHeader}>

                    <View style = {styles.listHeaderBackButtonHolder}>
                    </View>

                    <View style = {styles.listHeaderTitleHolder}>
                        <Text style={styles.listHeaderTitle}> My Tasks </Text>
                    </View>

                    <View style = {styles.listHeaderAddButtonHolder}>
                        <TouchableHighlight
                            style={styles.addButtonHolder}
                            onPress={this.onPressAdd}>
                            <Text style={styles.addButton}>Add</Text>
                        </TouchableHighlight>
                    </View>

                </View>

                <View style={styles.listHolder}>
                    <FlatList
                        ref = {'taskFlatList'}
                        data = {this.state.tasks}
                        keyExtractor = {item => item.id.toString()}
                        renderItem={({item}) => {
                            return (
                                <TaskListItem item={item} index={item.id} parentFlatList={this}>
                                </TaskListItem>);
                            }}
                    />

                    <AddTaskModal ref={'addModal'} parentFlatList={this}>

                    </AddTaskModal>

                    <EditTaskModal ref={'editModal'} parentFlatList={this}>

                    </EditTaskModal>
                </View>

            </View>
        );
    }
}
const styles = StyleSheet.create({
    listHolder: {
        flex: 1,
        backgroundColor: 'rgb(120, 120, 120)',
    },
    listCell: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: 'rgb(120, 120, 120)',
        height: 90,
    },
    listItemTitleHolder: {
        flex: 1,
        height: 30,
    },
    listItemSubtitleHolder: {
        flex: 1,
        flexDirection: 'row',
        height: 60
    },
    listItemLeftSubtitleHolder: {
        flex: 1,
        height: 60,
        textAlign: 'left',
    },
    listItemRightSubtitleHolder: {
        flex: 1,
        height: 60,
        textAlign: 'right',
    },
    listItemTitle: {
        flex: 1,
        color: 'rgb(255,140,0)',
        padding: 10,
        fontSize: 16,
    },
    listItemSubtitleLeft: {
        color: 'white',
        padding: 10,
        fontSize: 14,
    },
    listItemSubtitleRight: {
        color: 'white',
        padding: 10,
        fontSize: 14,
        marginRight: 10,
        textAlign: 'right',
    },
    listHeader: {
        backgroundColor: 'rgb(76, 76, 76)',
        height: 60,
        flexDirection: 'row',
    },
    listHeaderBackButtonHolder: {
        flex: 1,
        textAlign: 'left',
    },
    listHeaderTitleHolder: {
        flex: 1,
        textAlign: 'center',
        justifyContent: 'center',
        alignContent: 'center'
    },
    listHeaderAddButtonHolder: {
        flex: 1,
        textAlign: 'right',
        justifyContent: 'flex-end',
        alignContent: 'flex-end'
    },
    listHeaderTitle: {
        color: 'rgb(255,140,0)',
        fontSize: 20,
        alignSelf: 'center'
    },
    addButtonHolder: {
        height: 60,
        width: 60,
        marginRight: 10,
        padding: 10,
        alignSelf: 'flex-end',
        justifyContent: 'flex-end',
    },
    addButton: {
        flex: 1,
        color: 'rgb(255,140,0)',
        padding: 10,
        fontSize: 16,
    },
    listSeparator: {
        height: 1,
        backgroundColor: 'black'
    }
});
