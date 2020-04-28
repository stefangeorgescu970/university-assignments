'use strict';

import React, {Component} from 'react';
import {
    StyleSheet,
    Text,
    View,
    FlatList,
} from 'react-native';
import Swipeout from 'react-native-swipeout'
import {ServerTaskService} from '../Services/ServerTaskService.js';
import {MyStatusBar} from '../Misc/MyStatusBar.js';

class CompletedTaskListItem extends Component {

    constructor(props) {
        super(props);
        this.service = new ServerTaskService();
        this.state = {
            activeRowKey: null
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
                        const deletingRow = this.state.activeRowKey;
                        this.service.deleteTask(this.props.item, (success) => {
                            if (success == true) {
                                this.props.parentFlatList.handleDeleteTask(this.props.item);
                            }
                        });
                    },
                    text: 'Delete', type: 'delete'
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
    );
    }
}


export default class CompletedTaskListPage extends Component<{}> {

    constructor(props) {
        super(props);
        this.service = new ServerTaskService();
        this.state = ({
            tasks: [],
        });

        this.refreshList();
    }


    handleDeleteTask(oldTask) {
        this.refreshList();
    }


    refreshList() {
        this.service.getTasks(true, (receivedTasks) => {
            if (receivedTasks != null) {
                this.setState({tasks: receivedTasks});
            }
        })
    }

    render() {
        return(
            <View style={{flex: 1}}>
                <MyStatusBar backgroundColor="#4C4C4C" barStyle="light-content" />

                <View style={styles.listHeader}>


                    <View style = {styles.listHeaderTitleHolder}>
                        <Text style={styles.listHeaderTitle}> My Completed Tasks </Text>
                    </View>

                </View>

                <View style={styles.listHolder}>
                    <FlatList
                        ref = {'taskFlatList'}
                        data = {this.state.tasks}
                        keyExtractor = {item => item.id.toString()}
                        renderItem={({item}) => {
                            return (
                                <CompletedTaskListItem item={item} index={item.id} parentFlatList={this}>
                                </CompletedTaskListItem>);
                            }}
                    />

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
    listHeaderTitleHolder: {
        flex: 1,
        textAlign: 'center',
        justifyContent: 'center',
        alignContent: 'center'
    },
    listHeaderTitle: {
        color: 'rgb(255,140,0)',
        fontSize: 18,
        alignSelf: 'center'
    },
    listSeparator: {
        height: 1,
        backgroundColor: 'black'
    }
});
