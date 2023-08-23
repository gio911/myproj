import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddCurrentPaymentsDialogComponent } from './add-current-payments-dialog.component';

describe('AddCurrentPaymentsDialogComponent', () => {
  let component: AddCurrentPaymentsDialogComponent;
  let fixture: ComponentFixture<AddCurrentPaymentsDialogComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AddCurrentPaymentsDialogComponent]
    });
    fixture = TestBed.createComponent(AddCurrentPaymentsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
