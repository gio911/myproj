import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-current-payments-form',
  templateUrl: './current-payments-form.component.html',
  styleUrls: ['./current-payments-form.component.css']
})
export class CurrentPaymentsFormComponent implements OnInit{

  isNew = true

  form:FormGroup

  constructor(private route:ActivatedRoute){

  }

ngOnInit(): void {

  this.form = new FormGroup({
    counterparty:new FormControl(null, Validators.required)
  })

  this.route.params.subscribe((params:Params)=>{
    if(params['id']){
      //Editing
      this.isNew=false
    }
  })
}

onSubmit(){

}

}
