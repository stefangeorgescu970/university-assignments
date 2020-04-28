
import {Location} from '@angular/common';
import {Component} from '@angular/core';
import {AuthorService} from '../shared/author.service';

@Component({
  moduleId: module.id,
  selector: 'app-author-new',
  templateUrl: './author-new.component.html',
  styleUrls: ['./author-new.component.css']
})

export class AuthorNewComponent {
  constructor(private authorService: AuthorService,
              private location: Location) {

  }

  goBack(): void {
    this.location.back();
  }

  save(name): void {
    if (!this.isValid(name)) {
      return;
    }
    this.authorService.create(name)
      .subscribe(_ => this.goBack());
  }

  private isValid(name) {
    if (!name) {
      console.log('All input fields are required');
      alert('Please enter a name for the Author');
      return false;
    }
    return true;
  }
}
