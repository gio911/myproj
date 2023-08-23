import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CurrentPaymentsService } from '../shared/services/current-payments.service';
import { DatePipe } from '@angular/common';
import { ToastrService } from 'ngx-toastr';
import { MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  selector: 'app-add-current-payments-dialog',
  templateUrl: './add-current-payments-dialog.component.html',
  styleUrls: ['./add-current-payments-dialog.component.css']
})
export class AddCurrentPaymentsDialogComponent implements OnInit{

  paymentForm:FormGroup
  actionBtn:string='Сохранить'

  constructor(private datePipe: DatePipe, 
              private formBuilder:FormBuilder, 
              private currentPaymentService:CurrentPaymentsService,
              private toaster:ToastrService,
              private dialogRef:MatDialogRef<AddCurrentPaymentsDialogComponent>,
              @Inject(MAT_DIALOG_DATA) public editData:any,
              ){

}

ngOnInit(): void {
  this.paymentForm = this.formBuilder.group({
    counterparty:['', Validators.required],
    contract:['', Validators.required],
    date:['', Validators.required],
    num:['', Validators.required],
    sum:['', Validators.required],
    comment:['']

  })

  if(this.editData){
    this.actionBtn='Обновить'
    this.paymentForm.controls['counterparty'].setValue(this.editData.counterparty)
    this.paymentForm.controls['contract'].setValue(this.editData.contract)
    this.paymentForm.controls['date'].setValue(this.editData.date)
    this.paymentForm.controls['num'].setValue(this.editData.num)
    this.paymentForm.controls['sum'].setValue(this.editData.sum)
    this.paymentForm.controls['comment'].setValue(this.editData.comment)
  }
}

updatePayment(){
  console.log(this.paymentForm.value,  this.editData.id, 8885);
  
  this.currentPaymentService.putPayment(this.editData.id, this.paymentForm.value)
    .subscribe({
      next:(res)=>{
        this.toaster.success('Данный обновлены')
        this.paymentForm.reset()
        this.dialogRef.close('update')
      },
      error:(err)=>{
        console.log(err,777555);
        
        this.toaster.error('Ошибка при редактировании')
        
      }
    })
}


addPayment(){
    
  if(!this.editData){
    this.paymentForm.value['date'] = this.datePipe.transform(this.paymentForm.value['date'], 'yyyy-MM-ddTHH:mm:ss.sss')

  if(this.paymentForm.valid){
    this.currentPaymentService.createPayment(this.paymentForm.value)
      .subscribe({
        next:(res)=>{
             this.toaster.success('Платеж успешно добавлен')
             this.paymentForm.reset;
             this.dialogRef.close('save');

        },
        error:(err)=>{
          console.log(err);
          
        }
      })
    
    }
  }else{
    this.updatePayment()
 }
}
}
