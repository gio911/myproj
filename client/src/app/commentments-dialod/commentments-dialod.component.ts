import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Payment } from '../shared/interfaces';

@Component({
  selector: 'app-commentments-dialod',
  templateUrl: './commentments-dialod.component.html',
  styleUrls: ['./commentments-dialod.component.css']
})
export class CommentmentsDialodComponent implements OnInit {

  constructor(@Inject(MAT_DIALOG_DATA) public data:Payment, private ref:MatDialogRef<CommentmentsDialodComponent>){

  }

  incomePayment:Payment

  ngOnInit(): void {
    this.incomePayment = this.data
    console.log(this.incomePayment, 84848);
    
  }

  closeCommentmentDialog(){
    this.ref.close()
  }

}
