import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ResetComponent } from './reset.component';

const routes: Routes = [
  { path: '', component: ResetComponent, pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ResetRoutingModule {}
