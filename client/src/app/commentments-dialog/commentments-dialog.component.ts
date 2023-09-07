import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Commentment, Payment } from '../shared/interfaces';
import { ComentmentService } from '../shared/services/commentment.service';

@Component({
  selector: 'app-commentments-dialog',
  templateUrl: './commentments-dialog.component.html',
  styleUrls: ['./commentments-dialog.component.css']
})


export class CommentmentsDialodComponent implements OnInit {

  constructor(private commentmentService:ComentmentService, @Inject(MAT_DIALOG_DATA) public data:any, private ref:MatDialogRef<CommentmentsDialodComponent>){

  }
  incomePayment:any
  commentmentsArr:Commentment[]=[]
  addCommentmentValue:string=''
  commentmentObj: Commentment
  editCommentmentValue:string=''
  ngOnInit(): void {

    this.incomePayment = this.data.payment
    this.getAllCommentments(this.incomePayment.id)
    console.log(this.incomePayment, 84848);
    
  }

  getAllCommentments(id:number){
    this.commentmentService.getAllCommentments(id).subscribe({
      next:(res)=>{
        console.log(res, 884848322222);
        this.commentmentsArr=res
      },
      error:(err)=>{
        console.log(err);
        
      }
    })
  }

  addCommentment(){
    console.log(this.addCommentmentValue,54343);
    console.log(this.incomePayment, 995959559);
    
    this.commentmentObj={
      text:this.addCommentmentValue,
      id:1,
      isDone:false,
      date:new Date(),
      user_id:this.incomePayment.user_id,
      payment_id:this.incomePayment.id

    }
    this.commentmentService.addCommentment(this.commentmentObj).subscribe({
      next:()=>{  
        this.addCommentmentValue=''
        this.getAllCommentments(this.incomePayment.id)
      },
      error:(err)=>{
        console.log(err);
        
      }
    })

  }

  closeDialog(){

  }

  saveTask(){}
  // editCommentment(id:number){
  //   this.commentmentService.editCommentment(commentment).subscribe({
  //     next:()=>{
  //       this.getAllCommentments(this.incomePayment.id)
  //     },
  //     error:(err)=>{
  //       alert(err)
  //     }
  //   })
  // }

  deleteCommentment(id:number){
    this.commentmentService.deleteCommentment(id).subscribe({
      next:(res)=>{
        this.getAllCommentments(this.incomePayment.id)
      },
      error:(err)=>{
        alert(err)
      }
    })
  }

  closeCommentmentDialog(){
    this.ref.close()
  }

 call(commentment : Commentment) {
    this.commentmentObj = commentment;
    this.editCommentmentValue = commentment.text;
  }

}
