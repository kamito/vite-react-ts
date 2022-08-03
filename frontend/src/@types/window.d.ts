import { User } from './user.d'
import { Organization } from './organization.d'
import { Project } from './project.d'
import { Exapp } from './exapp.d'

interface InitData {
  user: User;
  organizaion: Organization;
  project: Project;
  app: Exapp;
  IS_DEBUG: boolean;
  IS_LOCAL: boolean;
}

interface Window {
  $INIT: string;
}

declare var window: Window
