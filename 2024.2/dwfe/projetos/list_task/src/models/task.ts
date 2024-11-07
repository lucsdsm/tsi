export  class  Task {
	name:  string;
	isComplete:  boolean;

	constructor(task  :  ITask) {
		this.name  =  task.name;
		this.isComplete  =  task.isComplete;
	}
}

interface  ITask{
	name:  string;
	isComplete:  boolean;
}