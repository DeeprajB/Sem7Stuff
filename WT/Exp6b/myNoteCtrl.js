angular.module("noteApp",[]).controller("NoteCtrl", ['$scope','$compile',function($scope,$compile) {
		let self=this;
		self.noteNum=0;
		self.takeNote=false;
		self.currentNote=null;

		self.newNote=function(){
			self.takeNote=true;
		}
		self.edit=function(noteNum){
			self.takeNote=true;
			let note=document.getElementById(`note${noteNum}`);
			document.getElementById("note-content").value=note.innerText;
			self.currentNote=note;
		}
		self.createAndPushNote=function(content){
			let notesContainer=document.getElementById('notes-container')
			let newNote=$compile(`
				<div class="note" id="note${self.noteNum}" ng-click="ctrl.edit(${self.noteNum})">
					${content}
					</div>
			`
		)($scope)
		self.noteNum+=1;
		angular.element(notesContainer).append(newNote);
		}
		self.leaveNote=function(){
			self.takeNote=false;
			document.getElementById("note-content").value="";
		}
		self.saveNote=function(){
			let noteContent=document.getElementById("note-content").value;
			if(self.currentNote==null){
				self.createAndPushNote(noteContent);
			}
			else{
				let p=self.currentNote
				if(noteContent==""){
					p.parentNode.removeChild(p)	;
				}
			else{
				p.innerHTML=noteContent;
			}
				self.currentNote=null;
			}
			self.leaveNote();
		}
}]);
